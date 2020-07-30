
from typing import List


class TimeZoneDatabase:
    ...


class Dimension:
    ...


class Language:
    @property
    def name(self) -> str: ...


class Locale:
    @property
    def name(self) -> str: ...


class DucklingTime:
    @property
    def iso8601(self) -> str: ...


class Context:
    reference_time: DucklingTime = ...
    locale: Locale = ...


def init(): ...
def stop(): ...
def load_time_zones(path: str) -> TimeZoneDatabase: ...
def get_current_ref_time(tz_db: TimeZoneDatabase, tz: str) -> DucklingTime: ...
def parse_ref_time(tz_db: TimeZoneDatabase, tz: str,
                   timestamp: int) -> DucklingTime: ...
def parse_lang(lang: str) -> Language: ...
def default_locale_lang(lang: Language) -> Locale: ...
def parse_locale(locale: str, default_locale: Locale) -> Locale: ...
def parse_dimensions(dims: List[str]) -> List[Dimension]: ...
def parse_text(text: str, context: Context, dimensions: List[Dimension],
               with_latent: bool = False) -> str: ...
