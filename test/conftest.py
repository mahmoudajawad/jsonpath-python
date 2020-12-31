import pytest
from collections import namedtuple

TestCase = namedtuple("TestCase", ("expr", "data", "result"))

data = {
    "a.b c": "a.b c",
    "book": [
        {
            "category": "reference",
            "author": "Nigel Rees",
            "title": "Sayings of the Century",
            "price": 8.95,
        },
        {
            "category": "fiction",
            "author": "Evelyn Waugh",
            "title": "Sword of Honour",
            "price": 12.99,
        },
        {
            "category": "fiction",
            "author": "Herman Melville",
            "title": "Moby Dick",
            "isbn": "0-553-21311-3",
            "price": 8.99,
        },
        {
            "category": "fiction",
            "author": "J. R. R. Tolkien",
            "title": "The Lord of the Rings",
            "isbn": "0-395-19395-8",
            "price": 22.99,
        },
    ],
    "bicycle": {"color": "red", "price": 19.95},
}

prices = [8.95, 12.99, 8.99, 22.99, 19.95]


@pytest.fixture(
    params=[
        TestCase("$.*", data, list(data.values())),
        TestCase("$.book", data, [data["book"]]),
        TestCase("$[book]", data, [data["book"]]),
        TestCase("$.'a.b c'", data, [data["a.b c"]]),
        TestCase("$['a.b c']", data, [data["a.b c"]]),
        TestCase("$..price", data, prices),
        TestCase("$.book[1:3]", data, data["book"][1:3]),
        TestCase("$.book[1:-1]", data, data["book"][1:-1]),
        TestCase("$.book[0:-1:2]", data, data["book"][0:-1:2]),
        TestCase("$.book[-1:1]", data, data["book"][-1:1]),
        TestCase("$.book[-1:-11:3]", data, data["book"][-1:-11:3]),
        TestCase("$.book[:]", data, data["book"][:]),
        TestCase("$.book[?(@.price>8 and @.price<9)].price", data, [8.95, 8.99]),
        TestCase('$.book[?(@.category=="reference")].category', data, ["reference"]),
        TestCase(
            '$.book[?(@.category!="reference" and @.price<9)].title',
            data,
            ["Moby Dick"],
        ),
        TestCase(
            '$.book[?(@.author=="Herman Melville" or @.author=="Evelyn Waugh")].author',
            data,
            ["Evelyn Waugh", "Herman Melville"],
        ),
    ]
)
def cases(request):
    return request.param
