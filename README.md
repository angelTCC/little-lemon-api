# little-lemon-api

```
little-lemon-api/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   ├── deps.py
│   │   └── v1/
│   │       ├── api.py
│   │       │
│   │       └── endpoints/
│   │           ├── auth.py
│   │           ├── users.py
│   │           ├── menu.py
│   │           ├── categories.py
│   │           ├── orders.py
│   │           └── reservations.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── permissions.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── menu.py
│   │   ├── order.py
│   │   ├── order_item.py
│   │   └── reservation.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── menu.py
│   │   ├── order.py
│   │   └── reservation.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── menu_repository.py
│   │   ├── order_repository.py
│   │   └── reservation_repository.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── menu_service.py
│   │   ├── order_service.py
│   │   └── reservation_service.py
│   │
│   ├── middleware/
│   │   ├── logging.py
│   │   └── rate_limit.py
│   │
│   ├── utils/
│   │   ├── pagination.py
│   │   ├── validators.py
│   │   └── helpers.py
│   │
│   └── tests/
│       ├── test_auth.py
│       ├── test_menu.py
│       ├── test_orders.py
│       └── conftest.py
│
├── alembic/
│
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── alembic.ini

```