
import React from "react"

import { useParams, useOutletContext } from "react-router";

import Error from "../Error/Error";
import Loading from "../Loading";
function Product() {
    const product = useOutletContext()
    
    const {id} = useParams()
    const Id = Number(id)
    const [productDetail, setProductDetail] = React.useState()
    const [errorMsg, setErrorMsg] = React.useState(null)
    const [loading, setLoading] = React.useState(true)
    if (product.errorMsg !== null) { 
    product.productInfoArray.forEach(item => {
        if (item.id === Id) {
            setProductDetail(item)
            setLoading(false)
        }
    })} else  {
        setErrorMsg(product.errorMsg)
        setLoading(false)
    }
    return (
        !loading ? (
        (errorMsg === null) ? (<>
        <h1>{productDetail.heading}</h1>
        <img src={productDetail.url} />
        <p>{productDetail.description}</p>
        <p>{productDetail.category.map((cat, index) => <span key={index}>{cat}</span>)}</p>
        <p>In stock: {productDetail.stock}</p>
        <button onClick={() => product.setCartDict((prev) => ({ ...prev, [Id]: (prev[Id] ?? 0) + 1 }))}>Add to Cart</button>
        <button>Buy now</button></>) : <Error type={500} /> ) : <Loading />
    )
}

export default Product;
