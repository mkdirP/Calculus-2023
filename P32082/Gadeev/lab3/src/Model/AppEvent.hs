module Model.AppEvent
    ( AppEvent(..)
    , handleEvent
    ) where

import Control.Lens
import Data.Fixed
import Monomer
import Monomer.Graph

import Model.AppModel

data AppEvent
    = AppInit
    | AppResetGraph
    | AppResetA
    | AppResetB
    | AppResetAccuracy
    | AppChangePointA Int (Double, Double)
    | AppChangePointB Int (Double, Double)
    | AppChangeAccuracy Int (Double, Double)
    | AppNChanged Int
    | AppRunge
    deriving (Eq, Show)

handleEvent :: AppEventHandler AppModel AppEvent
handleEvent _ _ model event = case event of
    AppInit ->
        [ Model $ model
            & currentResult .~ result1
            & prevResult .~ Nothing
            & rungeEnabled .~ True
        ]
    AppResetGraph -> [Message "mainGraph" GraphReset]
    AppResetA ->
        [ Model $ model & pointA .~ (-1)
        , Event AppInit
        ]
    AppResetB ->
        [ Model $ model & pointB .~ 1
        , Event AppInit
        ]
    AppResetAccuracy ->
        [ Model $ model & accuracy .~ 0.01
        , Event AppInit
        ]
    AppChangePointA _ (x, _) ->
        [ Model $ model & pointA .~ g x
        , Event AppInit
        ]
    AppChangePointB _ (x, _) ->
        [ Model $ model & pointB .~ g x
        , Event AppInit
        ]
    AppChangeAccuracy _ (x, _) ->
        [ Model $ model & accuracy .~ c x
        , Event AppInit
        ]
    AppNChanged _ -> [Event AppInit]
    AppRunge ->
        [ Model $ model
            & calcN *~ 2
            & currentResult .~ result2
            & prevResult .~ Just (model ^. currentResult)
            & rungeEnabled .~ rungeContinue
        ]
    where
        c = max 0.00001
        g x = (fromIntegral $ (div' x 0.01 :: Int))*0.01
        result1 = result n
        result2 = result $ 2*n
        result n' = compute (model ^. calcMethod) f a b n'
        f = fst $ functions!!(model ^. currentFunction)
        a = model ^. pointA
        b = model ^. pointB
        n = model ^. calcN
        rungeContinue = abs r >= e
        r = (result1-result2)/(2**k-1)
        k = if model ^. calcMethod == Simpson
            then 4
            else 2
        e = model ^. accuracy
