"""
test_store_analytics.py

Starter file for the "write your own tests" exercise.

pytest and the module under test are already imported below, and there's
one fully-worked example test to show you the pattern. Everything after
that is up to you: add your own test functions (name them test_something)
that check store_analytics.py against its docstrings.

Run your tests from this folder with:
    pytest -v
"""

import pytest
from store_analytics import (
    parse_order_row,
    compute_line_total,
    summarize_by_product,
    top_n_products,
    apply_bulk_discount,
    loyalty_tier,
    load_orders_from_csv,
    write_top_products_report,
)


# --- Example test (already written for you) -------------------------------

def test_parse_order_row_valid_row():
    row = ["1001", "Widget", "4", "9.99", "alice@example.com"]
    order = parse_order_row(row)
    assert order == {
        "order_id": "1001",
        "product": "widget",
        "quantity": 4,
        "unit_price": 9.99,
        "customer_email": "alice@example.com",
    }


# --- Your tests go below here ----------------------------------------------
#test 1: invalid rows

def test_parse_order_row_invalid_row():
    row = ["1001", "Widget", "4", "9.99"]
    with pytest.raises(ValueError):
        parse_order_row(row)
    
# test 2: using floats instead of int

def test_parse_order_row_different_quantity():
    row = ["1001", "Widget", "1.2", "9.99", "alice@example.com"]
    with pytest.raises(ValueError):
        parse_order_row(row)

# test 3: price becomes negative

def test_parse_order_row_negative_price():
    row = ["1001", "Widget", "4", "-2", "alice@example.com"]
    with pytest.raises(ValueError):
        parse_order_row(row)

# test 4: loyalty tier
# def loyalty_tier(total_spent):
    #
        #total_spent < 100            -> "none"
       # 100 <= total_spent < 500     -> "silver"
        #500 <= total_spent < 1000    -> "gold"
        #total_spent >= 1000          -> "platinum"
   # Raises ValueError if total spent is negative.

def test_loyalty_below_silver():
    assert loyalty_tier(99) == 'none'

def test_loyalty_at_silver():
    assert loyalty_tier(100) == 'none'

# test 5: n being negtaive for top_n_products(summary, n=3)
    # use placeholder values 
    # n = -1 
    def test_top_n_product():
        summary = {
            "item": {"total_quantity": 5, "total_revenue": 500, "order_count": 20}
        }
        with pytest.raises(ValueError)
            top_n_product(summary, n=-1)

