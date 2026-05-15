import React from "react";
import { useOutletContext } from "react-router";
import Error from "../Error/Error";
import Loading from "../Loading";
import { Link } from "react-router";

function Cart() {
  const [loading, setLoading] = React.useState(true)
  const [errorMsg, setErrorMsg] = React.useState(null)
  const [productsJSX, setProductsJSX] = React.useState()
  const value = useOutletContext()
  const numDict = value.cartDict
  if (value.errorMsg) {
    setErrorMsg(value.errorMsg)
    setLoading(false)
  }
  else {
    if (Object.keys(value.cartDict).length > 0) {
    setProductsJSX(value.productInfoArray.filter(item => item.id in value.cartDict).map(item => {
      
      return (
      <>
      <span>
        <img src={item.url} />
        <h1>{item.heading}</h1>
      </span>
      <button onClick={() => {value.setCartDict((prev) => ({ ...prev, [item.id]: prev[item.id] + 1 }))}}>{numDict[item.id]}</button>
      </>)
    }))}
  }
  return (!loading ? (errorMsg !== null ? (Object.keys(value.cartDict).length > 0 ? productsJSX: <p>Your cart is empty to add items to the cart browse through products on display on our website at <Link to="/">https://swiftly.com/</Link></p>): <Error type={500} /> ): {<Loading />})
}

export default Cart;
