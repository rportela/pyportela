from abc import abstractmethod
from pydantic import BaseModel


class DashboardItem(BaseModel):
    @abstractmethod
    def get_item_type(self) -> str:
        pass


class DashboardText(DashboardItem):
    text: str
    variant: str

    def get_item_type(self) -> str:
        return "text"


class Dashboard(BaseModel):
    id: str
    rows: list[DashboardItem] = list()

    def get_item_type(self) -> str:
        return "dashboard"


class DashboardRow(DashboardItem):
    cols: list[DashboardItem]

    def get_item_type(self) -> str:
        return "grid_row"


class DashboardGrid(DashboardItem):
    rows: list[DashboardItem]

    def get_item_type(self) -> str:
        return "grid"
