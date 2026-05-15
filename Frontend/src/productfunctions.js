import {updateProd, getAllProducts, getPrefProd, sellersSalesPerMonth, sellersAllProducts, getProdDetail, setProduct, kickUser, deleteProduct}  from "../../Backend"
export async function getAllProd() {
    try {
        const products = await getAllProducts()
        return products
    } catch(err) {
        return {error: err}
    }
}
export async function getPrefProducts(userId) {
    try {
        const prefProd = getPrefProd(userId)
        return prefProd
    } catch(err) {
        return {error: err}
    }
}
export async function getProductDetail(prodId) {
    
    try {
        
        const productDetails = getProdDetail(prodId)
        
        return productDetails
    } catch(err) {
        return {error: err}
    }
}
export async function getSellerSalesPerMonth(userId, num) {
    try {
        const productsDict = await sellersSalesPerMonth(userId, num)
        if (productsDict.successful) {
            return productsDict
        } else {
            const months = productsDict.months
            return {...productsDict, months}
        }
    } catch(err) {
        return {error: err}
    }
}
export async function getSellerDisplayedProducts(userId) {
    try {
        const sellersproducts = await sellersAllProducts(userId)
        return sellersproducts
    } catch(err) {
        return {error: err}
    }
}
export async function delUser(userId) {
    try {
        const val = await kickUser(userId)
        return val
    } catch(err) {
        return {error : err}
    }
}
export async function setProd(userId, product) {
    try {
        const val = await setProduct(userId, product)
        return val
    } catch (err) {
        return {error : err}
    }
}
export async function delProd(userId, prodId) {
    try {
        const val = await deleteProduct(userId, prodId)
        return val
    } catch(err) {
        return {error: err}
    }
}
export async function updateProduct(userId, prodId) {
    try {
        const val = await updateProd(userId, prodId)
        return val
    } catch (err) {
        return {error: err}
    }
}