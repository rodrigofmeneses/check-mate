from checkmate.user import User


def test_create_user_model_with_valid_data():
    data = {
        "username": "rfm",
        "email": "rfm@email.com",
        "password": "1234",
        "active": False,
    }
    user = User(**data)
    assert (
        all([user.username, user.email, user.password, user.active])
        is not None
    )


def test_create_user_model_with_missing_required_fields():
    data = {
        "username": "rfm",
    }
    user = User(**data)
    assert not any([user.email, user.password, user.avatar])
