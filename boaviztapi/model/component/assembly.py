from typing import Any

import boaviztapi.utils.roundit as rd
from boaviztapi.model.component.component import Component, NumberSignificantFigures


class ComponentAssembly(Component):
    IMPACT_FACTOR = {
        'gwp': {
            'impact': 6.68
        },
        'pe': {
            'impact': 68.60
        },
        'adp': {
            'impact': 1.41E-06
        }
    }

    def __init__(self, **kwargs):
        super().__init__()

    def impact_manufacture_gwp(self) -> NumberSignificantFigures:
        return self.__impact_manufacture('gwp')

    def __impact_manufacture(self, impact_type: str) -> NumberSignificantFigures:
        impact = self.IMPACT_FACTOR[impact_type]['impact']
        significant_figures = rd.min_significant_figures(impact)
        return impact, significant_figures

    def impact_manufacture_pe(self) -> NumberSignificantFigures:
        return self.__impact_manufacture('pe')

    def impact_manufacture_adp(self) -> NumberSignificantFigures:
        return self.__impact_manufacture('adp')

    def impact_use_gwp(self, model=None) -> NumberSignificantFigures:
        raise NotImplementedError

    def impact_use_pe(self, model=None) -> NumberSignificantFigures:
        raise NotImplementedError

    def impact_use_adp(self, model=None) -> NumberSignificantFigures:
        raise NotImplementedError

    @classmethod
    def from_dto(cls, arg: Any) -> 'ComponentAssembly':
        return cls()

    def to_dto(self, original_assembly: Any) -> Any:
        return original_assembly