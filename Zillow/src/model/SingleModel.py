import time
from model.LightGBM import LGB
from model.XGBoost import XGB
from model.RandomForest import RF
from model.ElasticNet import EN
from model.GradientBoostingRegressor import GBR
from model.LassoRegression import LR
from model.ExtraTreeRegressor import ETR
from model.SVR import SVR_
from model.GBREncoding import GBRE
from model.RidgeRegression import RR
from model.Keras import KR

class SingleModel:

    @staticmethod
    def __LaunchTraining(task,InputDir,OutputDir):

        d_model = {'lgb': LGB,
                   'xgb': XGB,
                   'rf': RF,
                   'en': EN,
                   'gbr': GBR,
                   'lr': LR,
                   'etr': ETR,
                   'svr': SVR_,
                   'gbre': GBRE,
                   'rr': RR,
                   'kr': KR
                   }

        start = time.time()

        model = d_model[task](InputDir,OutputDir)

        #print('Training %s begins ...' % task)
        #model.train()
        #print('Evaluation %s begins ...' % task)
        #model.evaluate()
        print('Summit %s begins ...' % task)
        model.submit()

        end = time.time()
        print('%s done, time elapsed %ds' % (task,(end - start)))

    @classmethod
    def run(cls,strategies,InputDir,OutputDir):

        start = time.time()
        for s in strategies:
            cls.__LaunchTraining(s,InputDir,OutputDir)
        end = time.time()
        print('\nAll tasks done, time consumed %ds' % (end - start))