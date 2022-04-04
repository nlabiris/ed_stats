import json
import dateutil.parser
from typing import List, Any, TypeVar, Callable, Type, cast
from datetime import datetime

T = TypeVar("T")

class Helper:
    @staticmethod
    def fromDatetime(x: Any) -> datetime:
        return dateutil.parser.parse(x)

    @staticmethod
    def fromString(x: Any) -> str:
        assert isinstance(x, str)
        return x

    @staticmethod
    def fromInteger(x: Any) -> int:
        assert isinstance(x, int) and not isinstance(x, bool)
        return x

    @staticmethod
    def toClass(c: Type[T], x: Any) -> dict:
        assert isinstance(x, c)
        return cast(Any, x).to_dict()

    @staticmethod
    def fromList(f: Callable[[Any], T], x: Any) -> List[T]:
        assert isinstance(x, list)
        return [f(y) for y in x]

    @staticmethod
    def fromBool(x: Any) -> bool:
        assert isinstance(x, bool)
        return x

    @staticmethod
    def fromFloat(x: Any) -> float:
        assert isinstance(x, (float, int)) and not isinstance(x, bool)
        return float(x)

    @staticmethod
    def fromNone(x: Any) -> Any:
        assert x is None
        return x

    @staticmethod
    def fromUnion(fs, x):
        for f in fs:
            try:
                return f(x)
            except:
                pass
        assert False

    def saveAsJSON(data, filename):
        '''
        Save data as JSON
        '''

        with open(filename, "w") as f:
            f.write(json.dumps(data))

    # TODO: Need the column names which will be each attribute of the dictionary data
    def saveAsCSV(data, columns, filename, separator=","):
        '''
        Save data as CSV
        '''

        with open(filename, "w") as f:
            f.write(separator.join(map(str, columns)) + "\n")
            for row in data:
                line = []
                for column in columns:
                    line.append(row[column])
                f.write(separator.join(map(str, line)) + "\n")
