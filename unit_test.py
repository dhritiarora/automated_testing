import pandas as pd
import pytest

df=pd.read_csv("df.csv")

def test_no_of_columns():
    assert (list(df.columns)) == ['Unnamed: 0','amt', 'city_pop', 'trans_hour', 'age', 'food_dining', 'gas_transport', 'grocery_net', 'grocery_pos', 'health_fitness', 'home','kids_pets', 'misc_net',  'misc_pos', 'personal_care', 'shopping_net', 'shopping_pos', 'travel', 'gender_M', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday','count_trans_90d','count_trans_24h', 'category_type_count','merchant_count','total_amt_30d','avg_amt_30d','amt_category_30d','merchant_amt_30d','amt_24h', 'is_fraud']


def test_gender_M() :
    assert df['gender_M'].unique().tolist()==[0,1]


def test_transaction_amt():
    assert df[df['amt']<0].shape[0]==0

def test_is_fraud():
    assert df['is_fraud'].unique().tolist()==[0,1]


