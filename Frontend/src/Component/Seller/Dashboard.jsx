/* eslint-disable react-hooks/exhaustive-deps */
import { useNavigate } from "react-router";
import { LineChart, XAxis, YAxis, CartesianGrid, Tooltip, Legend, Line } from 'recharts';
import { RechartsDevtools } from '@recharts/devtools';
import { useAuth } from "../../Contexts/authcontext";
import React from "react";
import { getSellerDisplayedProducts, getSellerSalesPerMonth } from "../../productfunctions";
import Error from "../Error/Error";
import Loading from "../Loading";

function SellerDashboard() {
  const num = [1, 3, 6, 12]
  
  const { currentUser} = useAuth()
  const [sellerProducts, setSellerProducts] = React.useState([])
  const [loading, setLoading] = React.useState(true)
  const [error, setError] = React.useState(null)
  const [months, setMonths] = React.useState(6)
  const [disableArr, setDisableArr] = React.useState([false, false, false, false])
  const [mincheck, setMinCheck] = React.useState(6)
  const [data, setData] = React.useState(null)
  const navigate = useNavigate()
  React.useEffect(() => {
    async function getprod() {
      setLoading(true)
      setMinCheck(6)
      setError(null)
      setDisableArr([false, false, false, false])
      const sellerProducts = await getSellerDisplayedProducts(currentUser.id)
      const salesperMonthDict = await getSellerSalesPerMonth(currentUser.id, months) 
      if ("error" in sellerProducts || "error" in salesperMonthDict) {
        setError(500)
        setLoading(false)
        return
      } if ("months" in salesperMonthDict) {
        setDisableArr(disableArr.map((i, ind) => num[ind] > months ? true : false))
        setMinCheck((num) => {
          for (let nu of num) {
            if (nu <= salesperMonthDict.months) {
              return nu
            }
          } 
          return 0
        })
      } 
      setSellerProducts(sellerProducts)
      setData(salesperMonthDict)
      setLoading(false)
    } 
    getprod() 
  }, [currentUser.id, months])
  function handleClick(event) {
    if (event.target.checked) {
      setMonths(Number(event.target.value))
    } 
  }
  return (
    (loading || data === null)? <Loading /> : error ? <Error type={error} />: <>
    {(mincheck !== 0 && sellerProducts.length !== 0) ? 
    <>
    <input type="checkbox" name="month" onChange={handleClick} value={num[0]} disabled={disableArr[0]} checked={num[0] === mincheck} />
    <input type="checkbox" name="month" onChange={handleClick} value={num[1]} disabled={disableArr[1]} checked={num[1] === mincheck} />
    <input type="checkbox" name="month" onChange={handleClick} value={num[2]} checked={num[2] === mincheck} disabled={disableArr[2]} />
    <input type="checkbox" name="month" onChange={handleClick} value={num[3]} disabled={disableArr[3]} checked={num[3] === mincheck} />
    <LineChart
    style={{ width: '100%', maxWidth: '700px', maxHeight: '70vh', aspectRatio: 1.618 }}
    responsive
    data={data}
    margin={{
      top: 5,
      right: 30,
      left: 20,
      bottom: 5,
    }}
  >
    <CartesianGrid strokeDasharray="3 3" />
    <XAxis dataKey="months" />
    <YAxis width="auto" />
    <Tooltip />
    <Legend />
    
    <Line type="monotone" dataKey="sales" stroke="#82ca9d" isAnimationActive={true} />
    <RechartsDevtools />
  </LineChart></> : <p>You have not displayed a single or more product continously for 1 month or more </p>}
    {sellerProducts.length !== 0 ? <>
    <h1>Your displayed products</h1>
    {sellerProducts.map(prod => {
      return (<>
      <img src={prod.url} />
      <h3>{prod.name}</h3>
      <div>{prod.stock}</div>
      <button onClick={() => navigate(`/product/${prod.id}`)}>Update product details</button>
      </>)
    })}</> : <p>You have no products displayed</p>}
    <button onClick={() => navigate("/product")}>Add product</button>
    </>
  )
}

export default SellerDashboard
