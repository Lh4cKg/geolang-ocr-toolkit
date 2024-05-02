import logging
import pathlib
import typing as typ


from .conf import settings
from .search import match


logger = logging.getLogger(__name__)


class BaseMatcher(object):

    def __init__(self, search_keywords: typ.List[str] = None,
                 save: bool = False):
        self.save = save
        if not search_keywords:
            self.search_keywords = self.load_search_keywords()
        else:
            if not isinstance(search_keywords, list):
                raise TypeError(f'`search_keywords` must be a list.')
            self.search_keywords = search_keywords

    def match(self):
        raise NotImplementedError

    @staticmethod
    def load_search_keywords() -> typ.List[str]:
        keywords_file = settings.INPUT_DIR / 'keywords.txt'
        if keywords_file.exists() is False:
            keywords_file.touch()
            # raise FileNotFoundError(
            #     f'`{keywords_file.name}` does not exists. '
            #     f'must be added to `{settings.INPUT_DIR}`.'
            # )
        with open(keywords_file) as f:
            return f.readlines()

    @staticmethod
    def save_file(filename: str, keyword: str) -> None:
        output_dir: pathlib.Path = settings.INPUT_DIR / 'matches.txt'
        if output_dir.exists() is False:
            output_dir.touch()

        with open(output_dir, 'a') as f:
            filename, page = filename.rsplit('-', 1)
            f.write(
                f'ფაილი: {filename} - '
                f'გვერდი: {page} - '
                f'ნაპოვნი საძიებო სიტყვა: "{keyword}"\n'
            )


class Matcher(BaseMatcher):

    def __init__(self, filename: str, text: str, save: bool = False,
                 search_keywords: typ.List[str] = None, threshold: int = None
                 ) -> None:
        super().__init__(search_keywords, save)
        self.filename = filename
        self.text = text
        self.threshold = threshold
        # TODO should be add exclude found journal logics

    def match(self) -> typ.Tuple[bool, int]:
        distance = 0
        for keyword in self.search_keywords:
            matched, distance = match(
                q1=self.text, q2=keyword, th=self.threshold
            )
            if matched:
                logger.info(f'This `{keyword}` matched in {self.filename} file.')
                if self.save is True:
                    self.save_file(self.filename, keyword)
                return matched, distance

        logger.info(f'Keywords does not matched in `{self.filename}` file.')
        return False, distance


class FileMatcher(BaseMatcher):

    def __init__(self, input_folder: typ.Union[str, pathlib.Path],
                 search_keywords: typ.List[str] = None) -> None:
        super().__init__(search_keywords)
        self.input_folder = input_folder
        # TODO will be add logic
