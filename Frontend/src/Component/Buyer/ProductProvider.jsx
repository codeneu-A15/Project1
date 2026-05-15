import React from "react"
import {Outlet} from "react-router"
import { getAllProd } from "../../productfunctions"
export default function ProductProvider() {
    
    const [errorMsg, setErrorMsg] = React.useState(null)
    const [cartDict, setCartDict] = React.useState({})
    const [productInfoArray, setProductInfoArray] = React.useState([])
    React.useEffect(() => {
        async function getAllProducts() {
            setErrorMsg(null)
            setCartDict({})
            setProductInfoArray([])
            const products = await getAllProd()
            if ("error" in products) {
                setErrorMsg(products.error)
                return
            }
            else {
                setCartDict(
                    products.reduce((acc, element) => ({ ...acc, [element.id]: 0 }), {})
                )
                setProductInfoArray(products)
        }}
        getAllProducts()
    }, [])
    
    const value = { productInfoArray, cartDict, setCartDict, ...(errorMsg !== null ? { errorMsg } : null) }
    return (
        <Outlet context={value} />
    )
}