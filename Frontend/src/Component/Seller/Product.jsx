import React from "react"
import Select from "react-select"
import { setProd } from "../../productfunctions"
import { useNavigate } from "react-router"
import { useAuth } from "../../Contexts/authcontext"
import Loading from "../Loading"
function Product() {
  const [error, setError] = React.useState(null)
  const [formError, setFormError] = React.useState(null)
  const [isSubmitting, setIsSubmitting] = React.useState(false)
  const {currentUser, loading} = useAuth()
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
  const [selected, setSelected] = React.useState([])
  const navigate = useNavigate()
  async function handleProduct(formData) {
    if (isSubmitting) {
      return 
    } if (selected.length === 0) {
      setFormError("you have to select atleast one category")
      return
    } if (loading || !currentUser) {
      setFormError("You need to sign up before registering your product")
      return
    }
    setFormError(null)
    setIsSubmitting(true)
    const productName = formData.get("productname")
    const productDetails = formData.get("productdetails")
    const categories = selected
    const stock = formData.get("stock")
    const product = {productName, productDetails, categories, stock, product}
    const val = await setProd(currentUser.id, product)
    if ("error" in val) {
      setError(val.error)
      
    } 
    setIsSubmitting(false)
  }
  
  return (
    <> {loading ? <Loading /> : <> 
    <form action={handleProduct}>
      <label for="productname">Product Name</label>
      <input type="text" id="productname" name="productname" />
      <label for="productname">Product Details</label>
      <textarea id="productdetails" name="productdetails"/>
      <label for="stock">How many in stock ?</label>
      <input type="number" id="stock" name="stock"/>
      <label for="categories">Categories</label>
      <Select options={categories} isMulti onChange={s => setSelected(s ? s.map(i => i.value).sort((a,b) => a.localeCompare(b)) : [])} name="stock" id="stock" />
      <button name="sumbit" disabled={isSubmitting}>Enter</button>
      <button name="cancel" type="button" onClick={() => navigate("/")}>Cancel</button>
    </form>
    {formError === null ? null : <h1>{formError}</h1>}
    {error === null ? null : <h1>Your product could not be added due to the error {error}</h1>}</>}
    </> 
  )
}

export default Product;
