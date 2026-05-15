/* eslint-disable */
import React from "react";
import { useParams } from "react-router";
import { useAuth } from "../../Contexts/authcontext";
import { getProductDetail, updateProduct } from "../../productfunctions";

export default function updateProducts() {
    const {id} = useParams()
    const categories = [
        { value: "electronics", label: "Electronics" },
        { value: "fashion", label: "Fashion" },
        { value: "home_appliances", label: "Home Appliances" },
        { value: "books", label: "Books" },
        { value: "toys", label: "Toys" },
        { value: "sports", label: "Sports" },
        { value: "beauty", label: "Beauty" },
        { value: "automotive", label: "Automotive" },
        { value: "groceries", label: "Groceries" },
        { value: "health", label: "Health" }
    ]
    const [count, setCount] = React.useState(0)
    const [selected, setSelected] = React.useState([])
    const [formError, setFormError] = React.useState(null)
    const [isSubmitting, setIsSubmitting] = React.useState(false)
    const [product, setProduct] = React.useState()
    const {currentUser, loading: load} = useAuth()
    const [error, setError] = React.useState()
    const [loading, setLoading] = React.useState(true)
    const [newProd, setNewProd] = React.useState(null)
    
    React.useEffect(() => {
        async function getData() {
            setLoading(true)
            const product = await getProductDetail(id)
            if ("error" in product) {
                setError(product.error)
                setLoading(false)
                return
            } else {
                setProduct(product)
                setNewProd(product)
            }
            setLoading(false)
        }
        getData()
    },[currentUser.id, id, count])
    async function handleSubmit(formData) {
        if (isSubmitting) {
            return
        }
        if (!currentUser || load) {
            setFormError("You must be authenticated to use this webpage") 
        }
        setIsSubmitting(true)
        
        setFormError(null)
        const productName = formData.get("productname")
        const productDetails = formData.get("productdetails")
        const categories = selected
        const stock = formData.get("stock")
        setNewProd(async () => await {productName, productDetails, categories, stock, product})
        if (newProd == product) {
            setFormError("You have make at least one change before updating the product")
            setIsSubmitting(false)
            return
        } else {
            
            const val = await updateProduct(currentUser.id, id)
            if ("error" in val) {
                setError(val.error)
            } else {
                setCount(count + 1)
            }
        }
        setIsSubmitting(false)
    }
    return (
    !loading ? error ? <Error type={500}/> : ( formError === "You must be authenticated to use this webpage" ? 
        <form action={handleSubmit}>
            <label for="productname">Product Name</label>
            <input type="text" id="productname" name="productname" value={product.name}/>
            <label for="productname">Product Details</label>
            <textarea id="productdetails" name="productdetails">{product.description}</textarea>
            <label for="stock">How many in stock ?</label>
            <input type="number" id="stock" name="stock" value={product.stock}/>
            <label for="categories">Categories</label>
            <Select options={categories} isMulti onChange={s => setSelected(s ? s.map(i => i.value).sort((a,b) => a.localeCompare(b)) : [])} name="stock" id="stock" defaultValue={categories.map(cat => cat.value in product.categories ? cat : false)}/>
            {formError === "You have make at least one change before updating the product"? <p>{formError}</p>: null }
            <button name="sumbit" disabled={isSubmitting}>Enter</button>
            <button name="cancel" type="button" onClick={() => navigate("/")}>Cancel</button>
        </form> : <p>{formError}</p>): <Loading />)
}