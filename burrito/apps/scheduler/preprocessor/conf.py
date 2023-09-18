from burrito.models.group_model import Groups
from burrito.models.statuses_model import Statuses
from burrito.models.faculty_model import Faculties
from burrito.models.queues_model import Queues
from burrito.models.permissions_model import Permissions
from burrito.models.roles_model import Roles
from burrito.models.role_permissions_model import RolePermissions


MODEL_KEYS = {
    "groups": Groups,
    "faculties": Faculties,
    "statuses": Statuses,
    "queues": Queues,
    "permissions": Permissions,
    "roles": Roles,
    "role_permissions": RolePermissions
}

DEFAULT_CONFIG = {
    "__tables_option": {
        "groups": "SELECT * FROM `groups`;",
        "faculties": "SELECT * FROM `faculties`;",
        "statuses": "SELECT * FROM `statuses`;",
        "queues": "SELECT * FROM `queues`;",
        "permissions": "SELECT * FROM `permissions`;",
        "roles": "SELECT * FROM `roles`;",
        "role_permissions": "SELECT * FROM `role_permissions`;"
    },
    "groups": [],     # will be updated automatic
    "faculties": [],  # will be updated automatic
    "statuses": [
        {"status_id": 1, "name": "NEW"},
        {"status_id": 2, "name": "ACCEPTED"},
        {"status_id": 3, "name": "OPEN"},
        {"status_id": 4, "name": "WAITING"},
        {"status_id": 5, "name": "REJECTED"},
        {"status_id": 6, "name": "CLOSE"}
    ],
    "queues": [
        {"queue_id": 100, "name": "Lecturers", "faculty_id": 335, "scope": "Reports"},
        {"queue_id": 101, "name": "Food", "faculty_id": 335, "scope": "Reports"},
        {"queue_id": 102, "name": "Scholarship", "faculty_id": 335, "scope": "Q/A"},
        {"queue_id": 103, "name": "Dormitory", "faculty_id": 335, "scope": "Q/A"},
        {"queue_id": 104, "name": "Dormitory", "faculty_id": 335, "scope": "Reports"},

        {"queue_id": 200, "name": "Lecturers", "faculty_id": 341, "scope": "Reports"},
        {"queue_id": 201, "name": "Food", "faculty_id": 341, "scope": "Reports"},
        {"queue_id": 202, "name": "Scholarship", "faculty_id": 341, "scope": "Q/A"},
        {"queue_id": 203, "name": "Dormitory", "faculty_id": 341, "scope": "Q/A"},
        {"queue_id": 204, "name": "Dormitory", "faculty_id": 341, "scope": "Reports"},

        {"queue_id": 300, "name": "Lecturers", "faculty_id": 345, "scope": "Reports"},
        {"queue_id": 301, "name": "Food", "faculty_id": 345, "scope": "Reports"},
        {"queue_id": 302, "name": "Scholarship", "faculty_id": 345, "scope": "Q/A"},
        {"queue_id": 303, "name": "Dormitory", "faculty_id": 345, "scope": "Q/A"},
        {"queue_id": 304, "name": "Dormitory", "faculty_id": 345, "scope": "Reports"},

        {"queue_id": 400, "name": "Lecturers", "faculty_id": 382, "scope": "Reports"},
        {"queue_id": 401, "name": "Food", "faculty_id": 382, "scope": "Reports"},
        {"queue_id": 402, "name": "Scholarship", "faculty_id": 382, "scope": "Q/A"},
        {"queue_id": 403, "name": "Dormitory", "faculty_id": 382, "scope": "Q/A"},
        {"queue_id": 404, "name": "Dormitory", "faculty_id": 382, "scope": "Reports"},

        {"queue_id": 500, "name": "Lecturers", "faculty_id": 383, "scope": "Reports"},
        {"queue_id": 501, "name": "Food", "faculty_id": 383, "scope": "Reports"},
        {"queue_id": 502, "name": "Scholarship", "faculty_id": 383, "scope": "Q/A"},
        {"queue_id": 503, "name": "Dormitory", "faculty_id": 383, "scope": "Q/A"},
        {"queue_id": 504, "name": "Dormitory", "faculty_id": 383, "scope": "Reports"},

        {"queue_id": 600, "name": "Lecturers", "faculty_id": 414, "scope": "Reports"},
        {"queue_id": 601, "name": "Food", "faculty_id": 414, "scope": "Reports"},
        {"queue_id": 602, "name": "Scholarship", "faculty_id": 414, "scope": "Q/A"},
        {"queue_id": 603, "name": "Dormitory", "faculty_id": 414, "scope": "Q/A"},
        {"queue_id": 604, "name": "Dormitory", "faculty_id": 414, "scope": "Reports"},
        {"queue_id": 605, "name": "Development", "faculty_id": 414, "scope": "Reports"},
        {"queue_id": 605, "name": "Development", "faculty_id": 414, "scope": "Q/A"},
        {"queue_id": 605, "name": "Development", "faculty_id": 414, "scope": "Suggestion"},

        {"queue_id": 700, "name": "Lecturers", "faculty_id": 1150, "scope": "Reports"},
        {"queue_id": 701, "name": "Food", "faculty_id": 1150, "scope": "Reports"},
        {"queue_id": 702, "name": "Scholarship", "faculty_id": 1150, "scope": "Q/A"},
        {"queue_id": 703, "name": "Dormitory", "faculty_id": 1150, "scope": "Q/A"},
        {"queue_id": 704, "name": "Dormitory", "faculty_id": 1150, "scope": "Reports"},

        {"queue_id": 800, "name": "Lecturers", "faculty_id": 1571, "scope": "Reports"},
        {"queue_id": 801, "name": "Food", "faculty_id": 1571, "scope": "Reports"},
        {"queue_id": 802, "name": "Scholarship", "faculty_id": 1571, "scope": "Q/A"},
        {"queue_id": 803, "name": "Dormitory", "faculty_id": 1571, "scope": "Q/A"},
        {"queue_id": 804, "name": "Dormitory", "faculty_id": 1571, "scope": "Reports"},

        {"queue_id": 900, "name": "Lecturers", "faculty_id": 1675, "scope": "Reports"},
        {"queue_id": 901, "name": "Food", "faculty_id": 1675, "scope": "Reports"},
        {"queue_id": 902, "name": "Scholarship", "faculty_id": 1675, "scope": "Q/A"},
        {"queue_id": 903, "name": "Dormitory", "faculty_id": 1675, "scope": "Q/A"},
        {"queue_id": 904, "name": "Dormitory", "faculty_id": 1675, "scope": "Reports"}
    ],
    "permissions": [
        {"permission_id": 1, "name": "UPDATE_PROFILE"},
        {"permission_id": 2, "name": "CREATE_TICKET"},
        {"permission_id": 3, "name": "READ_TICKET"},
        {"permission_id": 4, "name": "SEND_MESSAGE"},
        {"permission_id": 5, "name": "ADMIN"},
        {"permission_id": 6, "name": "GOD_MODE"}
    ],
    "roles": [
        {"role_id": 1, "name": "USER_ALL"},
        {"role_id": 2, "name": "USER_NO_M"},
        {"role_id": 3, "name": "USER_NO_CT"},
        {"role_id": 4, "name": "USER_NO_P"},
        {"role_id": 5, "name": "USER_NO_PCT"},
        {"role_id": 6, "name": "USER_NO_CTM"},
        {"role_id": 7, "name": "USER_NO_PM"},
        {"role_id": 8, "name": "USER_NO_PCTM"},
        {"role_id": 9, "name": "ADMIN"},
        {"role_id": 10, "name": "CHIEF_ADMIN"}
    ],
    "role_permissions": [
        {"role_id": 1, "permission_id": 1},
        {"role_id": 1, "permission_id": 2},
        {"role_id": 1, "permission_id": 3},
        {"role_id": 1, "permission_id": 4},

        {"role_id": 2, "permission_id": 1},
        {"role_id": 2, "permission_id": 2},
        {"role_id": 2, "permission_id": 3},

        {"role_id": 3, "permission_id": 1},
        {"role_id": 3, "permission_id": 3},
        {"role_id": 3, "permission_id": 4},

        {"role_id": 4, "permission_id": 2},
        {"role_id": 4, "permission_id": 3},
        {"role_id": 4, "permission_id": 4},

        {"role_id": 5, "permission_id": 3},
        {"role_id": 5, "permission_id": 4},

        {"role_id": 6, "permission_id": 1},
        {"role_id": 6, "permission_id": 3},

        {"role_id": 7, "permission_id": 2},
        {"role_id": 7, "permission_id": 3},

        {"role_id": 8, "permission_id": 3},

        {"role_id": 9, "permission_id": 1},
        {"role_id": 9, "permission_id": 2},
        {"role_id": 9, "permission_id": 3},
        {"role_id": 9, "permission_id": 4},
        {"role_id": 9, "permission_id": 5},

        {"role_id": 10, "permission_id": 1},
        {"role_id": 10, "permission_id": 2},
        {"role_id": 10, "permission_id": 3},
        {"role_id": 10, "permission_id": 4},
        {"role_id": 10, "permission_id": 5},
        {"role_id": 10, "permission_id": 6}
    ]
}
