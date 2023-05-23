module UI
    ( buildUI
    ) where

import Control.Lens
import Data.Maybe
import Monomer
import Monomer.EnhancedSlider
import Monomer.Graph
import TextShow

import Model

buildUI :: UIBuilder AppModel AppEvent
buildUI _ model = tree where
    tree = hstack_ [childSpacing_ 16]
        [ graphWithData_ points
            [ lockX_ $ model ^. xLock
            , lockY_ $ model ^. yLock
            ] `nodeKey` "mainGraph"
        , separatorLine
        , vstack_ [childSpacing_ 16]
            [ button "Reset" AppResetGraph
            , hgrid_ [childSpacing_ 64]
                [ labeledCheckbox "Lock X" xLock
                , labeledCheckbox "Lock Y" yLock
                ]
            , separatorLine
            , dropdown_ calcMethod methods methodTitle methodTitle
                [onChange (const AppInit :: Method -> AppEvent)]
            , dropdown currentFunction [0..length functions-1] et et
            , widgetIf (model ^. calcMethod == Simpson) $
                labeledCheckbox "Extend quadratic polys" extendS
            , separatorLine
            , hgrid_ [childSpacing_ 64]
                [ hstack_ [childSpacing_ 16]
                    [ label "a = "
                    , numericField_ pointA [onChange
                        (const AppInit :: Double -> AppEvent)]
                    ]
                , button "Reset" AppResetA
                ]
            , hgrid_ [childSpacing_ 64]
                [ hstack_ [childSpacing_ 16]
                    [ label "b = "
                    , numericField_ pointB [onChange
                        (const AppInit :: Double -> AppEvent)]
                    ]
                , button "Reset" AppResetB
                ]
            , hgrid_ [childSpacing_ 64]
                [ hstack_ [childSpacing_ 16]
                    [ label "e = "
                    , numericField_ accuracy
                        [ decimals 5
                        , minValue 0.00001
                        , onChange
                            (const AppInit :: Double -> AppEvent)
                        ]
                    ]
                , button "Reset" AppResetAccuracy
                ]
            , enhancedSlider_ calcN 1 42
                [ titleCaption "n"
                , onChange AppNChanged
                ]
            , separatorLine
            , label $ "I = " <> (showt integral)
            , widgetIf (not $ null $ model ^. prevResult) $
                vstack_ [childSpacing_ 16]
                    [ label $ "I' = " <> (showt prev)
                    , label $ "dI = " <> (showt $ integral-prev)
                    ]
            , button "Next Runge iteration" AppRunge
                `nodeEnabled` (model ^. rungeEnabled)
            ] `styleBasic` [sizeReqW $ fixedSize 300]
        ] `styleBasic` [padding 16]
    points =
        [
            [ graphPoints $ (\x -> (x, f x)) <$> xs
            , graphColor red
            ]
        ,   [ graphPoint (a, 0)
            , graphColor blue
            , graphHoverColor lightBlue
            , graphActiveColor darkBlue
            , graphWidth 4
            , graphSeparate
            , graphOnChange AppChangePointA
            ]
        ,   [ graphPoint (b, 0)
            , graphColor green
            , graphHoverColor lightGreen
            , graphActiveColor darkGreen
            , graphWidth 4
            , graphSeparate
            , graphOnChange AppChangePointB
            ]
        ] <> (makeShape . fromIntegral <$> [0..n-1]) <> simps
    makeShape i =
        [ graphPoints $ addBounds i $ case (model ^. calcMethod) of
            RectangleLeft ->
                [ (h*i+a, f $ h*i+a)
                , (h*(i+1)+a, f $ h*i+a)
                ]
            RectangleMiddle ->
                [ (h*i+a, f $ h*(i+0.5)+a)
                , (h*(i+1)+a, f $ h*(i+0.5)+a)
                ]
            RectangleRight ->
                [ (h*i+a, f $ h*(i+1)+a)
                , (h*(i+1)+a, f $ h*(i+1)+a)
                ]
            Trapezoid ->
                [ (h*i+a, f $ h*i+a)
                , (h*(i+1)+a, f $ h*(i+1)+a)
                ]
            Simpson -> quadF (h*i+a) <$>
                [h*i+a, (h*i+a+0.02)..(h*(i+1)+a)]
        , graphColor orange
        , graphFill
        ]
    simps = if model ^. calcMethod == Simpson && model ^. extendS
        then makeSimp . fromIntegral <$> [0..n-1]
        else []
    makeSimp i =
        [ graphPoints $ quadF (h*i+a) <$>
            [h*i+a-h/3, (h*i+a+0.02-h/3)..(h*(i+1)+a+h/3)]
        , graphColor $ (cycle [brown, green, blue])!!(floor i)
        , graphWidth 4
        ]
    addBounds i ps = ((h*i+a, 0):ps) <> [(h*(i+1)+a, 0)]
    quadF t x = (x, (f t)*t'+(f m)*m'+(f q)*q') where
        t' = (x-m)*(x-q)/(t-m)/(t-q)
        m' = (x-t)*(x-q)/(m-t)/(m-q)
        q' = (x-t)*(x-m)/(q-t)/(q-m)
        m = (t+q)/2
        q = t+h
    h = (b-a)/(fromIntegral n)
    a = round' $ model ^. pointA
    b = round' $ model ^. pointB
    integral = round' $ model ^. currentResult
    prev = round' $ fromJust $ model ^. prevResult
    round' x = (fromIntegral $ (round (x*bn) :: Integer))/bn
    bn = 1000000
    n = model ^. calcN
    f = fst $ functions!!(model ^. currentFunction)
    xs = [-20, -19.98..20]
    methods =
        [ RectangleLeft
        , RectangleMiddle
        , RectangleRight
        , Trapezoid
        , Simpson
        ]
    methodTitle t = label $ case t of
        RectangleLeft -> "Left rectangles"
        RectangleMiddle -> "Middle rectangles"
        RectangleRight -> "Right rectangles"
        Trapezoid -> "Trapezoids"
        Simpson -> "Simpson"
    et t = label $ snd $ functions!!t
