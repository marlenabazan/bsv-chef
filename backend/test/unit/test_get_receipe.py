import pytest
import unittest.mock as mock

from src.controllers.receipecontroller import ReceipeController
from src.static.diets import Diet

receipe = {
    "name": "Banana Bread",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Butter": 100,
        "Banana": 4,
        "Sugar": 200,
        "Egg": 1,
        "Vanilla Sugar": 1,
        "Baking Powder": 0.5,
        "Salt": 5,
        "Cinnamon": 10,
        "Flour": 220,
        "Walnuts": 10
    }
}

@pytest.fixture
def sut():
    mocked_dao = mock.MagicMock()
    mocked_controller = ReceipeController(mocked_dao)

    return mocked_controller


@pytest.mark.unit
def test_returns_readiness_below_threshold_and_right_diet(sut):

    available_items = {
        "Butter": 100
    }

    diet = Diet.NORMAL

    with mock.patch("src.controllers.receipecontroller.calculate_readiness") as mocked_calculate_readiness:
        mocked_calculate_readiness.return_value = 0.01

        readiness = sut.get_receipe_readiness(receipe, available_items, diet)

    assert readiness == None


@pytest.mark.unit
def test_returns_readiness_below_threshold_and_wrong_diet(sut):

    available_items = {
        "Butter": 100
    }

    diet = Diet.VEGAN

    with mock.patch("src.controllers.receipecontroller.calculate_readiness") as mocked_calculate_readiness:
        mocked_calculate_readiness.return_value = 0.01

        readiness = sut.get_receipe_readiness(receipe, available_items, diet)

    assert readiness == None


@pytest.mark.unit
def test_returns_readiness_1_and_right_diet(sut):

    available_items = {
        "Butter": 100,
        "Banana": 4,
        "Sugar": 200,
        "Egg": 1,
        "Vanilla Sugar": 1,
        "Baking Powder": 0.5,
        "Salt": 5,
        "Cinnamon": 10,
        "Flour": 220,
        "Walnuts": 10
    }

    diet = Diet.NORMAL

    with mock.patch("src.controllers.receipecontroller.calculate_readiness") as mocked_calculate_readiness:
        mocked_calculate_readiness.return_value = 1.0

        readiness = sut.get_receipe_readiness(receipe, available_items, diet)

    assert readiness == 1.0

@pytest.mark.unit
def test_returns_readiness_0_1_and_right_diet(sut):

    available_items = {
        "Butter": 100,
        "Banana": 4,
        "Sugar": 200,
        "Egg": 1,
        "Vanilla Sugar": 1,
        "Baking Powder": 0.5,
        "Salt": 5,
        "Cinnamon": 10,
        "Flour": 220,
        "Walnuts": 10
    }

    diet = Diet.NORMAL

    with mock.patch("src.controllers.receipecontroller.calculate_readiness") as mocked_calculate_readiness:
        mocked_calculate_readiness.return_value = 0.1

        readiness = sut.get_receipe_readiness(receipe, available_items, diet)

    assert readiness == 0.1


@pytest.mark.unit
def test_returns_None_when_wrong_diet(sut):

    available_items = {
        "Butter": 100,
        "Banana": 4,
        "Sugar": 200,
        "Egg": 1,
        "Vanilla Sugar": 1,
        "Baking Powder": 0.5,
        "Salt": 5,
        "Cinnamon": 10,
        "Flour": 220,
        "Walnuts": 10
    }

    diet = Diet.VEGAN

    with mock.patch("src.controllers.receipecontroller.calculate_readiness") as mocked_calculate_readiness:
        mocked_calculate_readiness.return_value = 1.0

        readiness = sut.get_receipe_readiness(receipe, available_items, diet)

    assert readiness == None
