{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Move map inside list comprehension" #-}
{-# HLINT ignore "Use infix" #-}
import System.IO
import System.Environment
import Control.Monad
import Data.List
import Data.Function

(|*|) :: [[Double]] -> [Double] -> [Double]
(|*|) mA mB = map (sum . zipWith (*) mB) mA

(|-|) :: [Double] -> [Double] -> [Double]
(|-|) = zipWith (-)

round' :: Double -> Double
round' x = fromIntegral (round (x*10^6)) / 10^6

show'' :: Bool -> [Double] -> String
show'' vline xs = f (map (show . round') xs) where
    f [] = ""
    f [a] = if vline then "| " ++ a else a
    f (a:as) = a ++ replicate (16 - length a) ' ' ++ f as

show' :: [Double] -> String
show' = show'' False

showM :: [[Double]] -> IO ()
showM = mapM_ (putStrLn . show'' True)

swap :: [a] -> Int -> Int -> [a]
swap xs i j = zipWith f [0..] xs where
    f k x
        | k == i = xs!!j
        | k == j = xs!!i
        | otherwise = x

chooseMain :: [[Double]] -> Int -> ([[Double]], Bool)
chooseMain matrix i = (swap matrix i j, i /= j) where
    f = compare `on` abs . (!!i) . (matrix!!)
    j = maximumBy f [i..length matrix-1]

exclude :: [[Double]] -> Int -> [[Double]]
exclude matrix i = take (i+1) matrix ++ map f (drop (i+1) matrix) where
    h    = matrix!!i!!i
    f xs = if xs!!i == 0 then xs
        else zipWith (\a x -> a*q+x) (matrix!!i) xs where q = -xs!!i/h

stepForward :: [[Double]] -> Int -> ([[Double]], Bool)
stepForward matrix i = (exclude m i, s) where
    (m, s) = chooseMain matrix i

gaussForward :: [[Double]] -> ([[Double]], Integer)
gaussForward matrix = gaussForward' matrix 0 where
    gaussForward' m i = if i == length m then (m, 0)
        else (mT, if s then ss+1 else ss) where
            (m', s) = stepForward m i
            (mT, ss) = gaussForward' m' (i+1)

gaussBack :: [[Double]] -> [Double]
gaussBack matrix = gaussBack' [] where
    gaussBack' xs = if n == length matrix then xs
        else gaussBack' (x:xs) where
            n = length xs
            i = length matrix - n - 1
            b = last (matrix!!i)
            x = (b - sum (zipWith (*) (drop (i+1) (matrix!!i)) xs))/matrix!!i!!i

residual :: [[Double]] -> [Double] -> [Double] -> [Double]
residual mA mB mX = mA |*| mX |-| mB

determinant :: [[Double]] -> Double
determinant [a] = head a
determinant matrix = sum (map f [1..n]) where
    n       = length matrix
    f i     = minor i * head (matrix!!(i-1)) * (-1)^(i-1)
    minor i = determinant ([(tail . (matrix !!)) (j - 1) | j <- [1 .. n], i /= j])

parse :: String -> [Double]
parse = map read . words

showGaussForward :: [[Double]] -> Int -> IO ([[Double]], Integer)
showGaussForward matrix 1 = return (matrix, 0)
showGaussForward matrix i = do
    let step = length matrix - i + 1
    putStrLn ("Шаг " ++ show step)
    let (t, s) = chooseMain matrix (step-1)
    let t' = exclude t (step-1)
    putStrLn "Выбираем главный элемент:"
    showM t
    if s
        then return ()
        else putStrLn "Ничего менять местами не пришлось."
    putStrLn ("Исключим x" ++ show step ++ " из остальных уравнений:")
    showM t'
    (mT, ss) <- showGaussForward t' (i-1)
    if s
        then return (mT, ss+1)
        else return (mT, ss)

main :: IO ()
main = do
    args <- getArgs
    firstLine <- getLine
    let firstRow = parse firstLine
    let n        = length firstRow-1
    tailRows <- replicateM (n-1) $ parse <$> getLine
    let matrix   = firstRow : tailRows
    let mA       = map init matrix
    let mB       = map last matrix
    let det      = determinant mA
    (mT, ss) <- if "--show" `elem` args
        then showGaussForward matrix n
        else let (mT, ss) = gaussForward matrix in
            (putStrLn "Треугольная матрица после прямого хода:"
                >> showM mT
                >> return (mT, ss))
    putStrLn ("Перестановок: " ++ show ss)
    let det' = (-1)^ss*product [mT!!i!!i | i <- [0..n-1]]
    putStr "Определитель: "
    print det'
    when (elem "--det" args) $ do
            putStr "Определитель, посчитанный неоптимизированно: "
            print det
    if det' == 0
        then putStrLn "Определитель нулевой, решить нельзя."
        else do
            let mX = gaussBack mT
            putStrLn ("Вектор неизвестных: " ++ show' mX)
            putStrLn ("Вектор невязок:     " ++ show' (residual mA mB mX))
