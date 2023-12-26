from pydantic import BaseModel, Field


class LossItemModel(BaseModel):
    date: str
    tanks: int = Field(alias="Танки")
    bbms: int = Field(alias="ББМ")
    canons: int = Field(alias="Гармати")
    mlrs: int = Field(alias="РСЗВ")
    ppo: int = Field(alias="Засоби ППО")
    aircrafts: int = Field(alias="Літаки")
    helicopters: int = Field(alias="Гелікоптери")
    ucavs: int = Field(alias="БПЛА")
    cruise_missils: int = Field(alias="Крилаті  ракети")
    ships: int = Field(alias="Кораблі (катери)")
    submarines: int = Field(alias="Підводні човни")
    cars: int = Field(alias="Автомобілі та автоцистерни")
    special_machines: int = Field(alias="Спеціальна техніка")
    personnel: int = Field(alias="Особовий склад")
