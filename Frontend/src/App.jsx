import React from "react"
import UpdateProducts from "./Component/Seller/Updateproducts"
import {BrowserRoutes} from "react-router-dom"
import LandingPage from "./Component/Homepage"
import SignUp from "./Component/Auth/Signup"
import SignIn from "./Component/Auth/SignIn"
import Products from "./Component/Buyer/Products"
import Product from "./Component/Buyer/Product"
import Cart from "./Component/Buyer/Cart"
import Buy from "./Component/Buyer/Buy"
import AdminPage from "./Component/Admin/Admin"
import SellerDashboard from "./Component/Seller/Dashboard"
import Contact from "./Component/ContactUs"
import Error from "./Component/Error/Error"
import { AuthProvider } from "./Contexts/authcontext"

function App() {
    return (
    <AuthProvider>
    <BrowserRoutes>
        <Routes>
            <Route index element={<LandingPage />}/>
            <Route path="/Signup" element={<SignUp />} />
            <Route element={<ProtectedRoute type="buyer" />}>
                <Route path="/products" element={<Products />}/>
                <Route element={<ProductProvider />}>
                <Route path="/product/buyer/:id" element={<Product />} />
                <Route path="/cart" element={<Cart />} />
                <Route path="/buy" element={<Buy />} />
                <Route path="/buy/:id" element={<BuyOne />} />
                </Route>
            </Route>
            <Route path="/SignIn" element={<SignIn />} />
            <Route element={<ProtectedRoute type="admin"/>}>
                <Route path="/admin" element={<AdminPage />} />
            </Route>
            
            <Route element={<ProtectedRoute type="seller"/>}>
                <Route path="/dashboard" element={<SellerDashboard />} />
                <Route path="/product" element={<Product />}/>
                <Route path="/product/:id" element={<UpdateProducts />} />
            </Route>
            
            <Route path="*" element={<Error type={404} />} />
        </Routes>
    </BrowserRoutes>
    </AuthProvider>
)}

export default App
