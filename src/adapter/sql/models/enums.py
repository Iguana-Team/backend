from enum import Enum

class FuncBlockEnum(Enum):
    CORPORATE = 'Корпоративный блок'
    RETAIL = 'Розничный блок'


class Division4Enum(Enum):
    OFFICE1 = 'Дополнительный офис 1'
    OFFICE2 = 'Дополнительный офис 2'
    OFFICE3 = 'Дополнительный офис 3'
    OFFICE4 = 'Дополнительный офис 4'


class RoleEnum(Enum):
    LEADERSHIP = 'руководство'
    DESIGNER = 'Дизайнер'
    ANALYST = 'аналитика'
    BACKEND = 'backend'
    FRONTEND = 'frontend'
    TESTER = 'тестирование'
    BACKOFFICE = 'бэк-офис'
    SALES = 'продажи'
    SERVICE = 'обслуживание'


class UserPermissionEnum(Enum):
    USER = 'user'
    ADMIN = 'admin'