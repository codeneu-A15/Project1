import React from "react"
import './App.css'
import {BrowserRoutes} from "raect-router-dom"
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

function App() {
    <BrowserRoutes>
        <Routes>
            <Route index element={<LandingPage />}/>
            <Route path="Signup" element={<SignUp />} />
            <Route path="Login" element={<SignIn />} />
            <Route path="products" element={<Products />}/>
            <Route path="product/buyer/:id" element={<Product />} />
            <Route path="cart" element={<Cart />} />
            <Route path="buy" element={<Buy />} />
            <Route path="admin" element={<AdminPage />} />
            <Route path="Dashboard" element={<SellerDashboard />} />
            <Route path="contactUs" element={<Contact />} />
            <Route path="product/seller/:id" />
            <Route path="*" element={<Error type={404} />} />
        </Routes>
    </BrowserRoutes>
}

export default App
