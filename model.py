# 导入数据
import ipdb
from sklearn.datasets import load_boston

# 导入常用模型包
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import xgboost as xgb


def xgb_test():
    data = load_boston()
    x, y = data['data'], data['target']
    x_train, x_valid, y_train, y_valid = train_test_split(x, y, test_size=0.2, random_state=2019)
    # 创建xgb矩阵
    d_x = xgb.DMatrix(x_train)
    d_y = xgb.DMatrix(y_train.reshape(-1, 1))

    xgbr = xgb.XGBRegressor()
    xgbr.fit(x_train, y_train)
    
    pred = xgbr.predict(x_valid)
    return mean_squared_error(y_valid, pred)
