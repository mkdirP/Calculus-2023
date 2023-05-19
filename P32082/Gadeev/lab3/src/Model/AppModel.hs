{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE FunctionalDependencies #-}
{-# LANGUAGE TemplateHaskell #-}

module Model.AppModel
    ( module Model.Method
    , AppModel(..)
    , xLock
    , yLock
    , calcMethod
    , currentFunction
    , pointA
    , pointB
    , calcN
    , accuracy
    , extendS
    , currentResult
    , prevResult
    , rungeEnabled
    , initModel
    , functions
    ) where

import Control.Lens
import Data.Text (Text)

import Model.Method

data AppModel = AppModel
    { _amXLock :: Bool
    , _amYLock :: Bool
    , _amCalcMethod :: Method
    , _amCurrentFunction :: Int
    , _amPointA :: Double
    , _amPointB :: Double
    , _amCalcN :: Int
    , _amAccuracy :: Double
    , _amExtendS :: Bool
    , _amCurrentResult :: Double
    , _amPrevResult :: Maybe Double
    , _amRungeEnabled :: Bool
    } deriving (Eq, Show)

makeLensesWith abbreviatedFields 'AppModel

initModel :: AppModel
initModel = model where
    model = AppModel
        { _amXLock = False
        , _amYLock = False
        , _amCalcMethod = RectangleLeft
        , _amCurrentFunction = 0
        , _amPointA = -1
        , _amPointB = 1
        , _amCalcN = 4
        , _amAccuracy = 0.01
        , _amExtendS = False
        , _amCurrentResult = integral
        , _amPrevResult = Nothing
        , _amRungeEnabled = True
        }
    integral = compute RectangleLeft f (-1) 1 4
    f = fst $ head functions

functions :: [(Double -> Double, Text)]
functions =
    [ (\x -> -3*(x**3)-5*(x**2)+4*x-2, "f(x) = -3x^3-5x^2+4x-2")
    , (\x -> sin x, "f(x) = sin(x)")
    , (\x -> (sin $ x**2), "f(x) = sin(x^2)")
    , (\x -> exp (-x**2), "f(x) = e^(-x^2)")
    , (\x -> (sin x)/x, "f(x) = sin(x)/x")
    , (\x -> x, "f(x) = x")
    , (\x -> (log x)*(cos x), "f(x) = ln(x)cos(x)" )
    , (\x -> 1/x, "f(x) = 1/x")
    ]
