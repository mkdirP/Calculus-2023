module Model.Method
    ( Method(..)
    , compute
    ) where

data Method
    = RectangleLeft
    | RectangleMiddle
    | RectangleRight
    | Trapezoid
    | Simpson
    deriving (Eq, Show)

geth :: Double -> Double -> Int -> Double
geth a b n = (b-a)/(fromIntegral n)

getxi :: Double -> Double -> Int -> [Double]
getxi a b n = [a+(fromIntegral i)*h | i <- [0..n]] where
    h = geth a b n

compute
    :: Method
    -> (Double -> Double)
    -> Double
    -> Double
    -> Int
    -> Double
compute RectangleLeft f a b n = h*(sum (map f xm)) where
    h = geth a b n
    xm = [xi!!(i-1) | i <- [1..n]]
    xi = getxi a b n
compute RectangleMiddle f a b n = h*(sum (map f xm)) where
    h = geth a b n
    xm = [(xi!!(i-1)+xi!!i)/2 | i <- [1..n]]
    xi = getxi a b n
compute RectangleRight f a b n = h*(sum (map f xm)) where
    h = geth a b n
    xm = [xi!!i | i <- [1..n]]
    xi = getxi a b n
compute Trapezoid f a b n = h*(ends+sum(map f xm)) where
    h = geth a b n
    ends = (f (xi!!0) + f (xi!!n))/2
    xm = tail $ init xi
    xi = getxi a b n
compute Simpson f a b n = h/3*(ends+4*odds+2*evens) where
    h = geth a b n
    ends = f (xi!!0) + f (xi!!n)
    odds = sum $ map (f . (xi!!)) [1, 3..n-1]
    evens = sum $ map (f . (xi!!)) [2, 4..n-2]
    xi = getxi a b n
