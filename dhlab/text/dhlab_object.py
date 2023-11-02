from typing import Union
import pandas as pd
from abc import ABC, abstractmethod


class DhlabObj(ABC):
    """DHLAB base class

    Provides shared utility methods to DHLAB classes.
    """

    def __init__(self, frame : pd.DataFrame = pd.DataFrame()):
        self.frame = frame

        # self.size = None
        # if isinstance(frame, pd.DataFrame):
        #     self.size = len(frame)

    @property
    def size(self):
        return len(self.frame)
    
    @property
    def loc(self):
        return self.frame.loc
    
    def make_subset(self, row_slice, col_slice):
        return self.from_df(self.frame.loc[:, col_slice].iloc[row_slice])
    
    def __getitem__(self, *args, **kwargs):
        return self.from_df(self.frame.__getitem__(*args, **kwargs))
    
    def __repr__(self) -> str:
        """
        Return the string representation of the  DhlabObj frame attribute
        """
        return self.frame.__repr__()

    def _repr_html_(self) -> Union[str, None]:
        """
        Return the HTML representation of the DhlabObj frame attribute
        """
        return self.frame._repr_html_()

    def head(self, n=5):
        return self.from_df(self.frame.head(n))

    def tail(self, n=5):
        return self.from_df(self.frame.tail(n))

    def sort(self, by=None, asc=False):
        if by is None:
            by = self.frame.columns[0]
        return self.from_df(self.frame.sort_values(by=by, ascending=asc))

    def to_csv(self, path):
        self.frame.to_csv(path, index=None)

    def to_excel(self, path):
        self.frame.to_excel(path, index=None)

    @abstractmethod
    def from_df(cls, df):
        pass

    @classmethod
    def from_csv(cls, path):
        df = pd.read_csv(path)
        return cls.from_df(df)