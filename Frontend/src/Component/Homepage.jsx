import React from "react";
import { useAuth } from "../Contexts/authcontext";
import Loading from "./Loading";
import { Link } from "react-router";
import {image1} from "https://unsplash.com/photos/a-foggy-forest-filled-with-lots-of-trees-I8Sfln1u0S4"
import {image2} from "https://unsplash.com/photos/black-and-white-love-print-textile-1GxdTleoEls"
function LandingPage() {
  const time1 = new Date().getTime()
  const {loading} = useAuth()
  const [error, setError] = React.useState(null)
  while (true) {
    if (!loading) {
      break
    } else {
      const time2 = new Date().getTime()
      if ((time2 - time1) > 4000) {
        setError("The website took too long to respond")
      }
    }
  }
  return (
    loading ? <Loading /> : error !== null ? <>
      <header>
        <h1>Swiftly</h1>
        <button>About us</button>
        <button>Code of Conduct</button>
        <Link to="/SignIn">Sign In</Link>
        <Link to="/Signup">Sign Up</Link>
      </header>
      <main>
        <div className="Hero">
          <h1>Swiftly</h1>
          <h2>Your go to hassle Free Ecommerce website</h2>
        </div>
        <div className="AboutUs">
          <h2>About us</h2>
          <div className="1">
            <img src={image1}/>
            <h3>Hassle Free</h3>
            <p>We provide hassle free service for both buyers and sellers alike</p>
          </div>
          <div className="2">
            <img src={image2} />
            <h3>No Ads</h3>
            <p>We do not display adds on our website</p>
          </div>
        </div>
        <div className="code">
          <h1>Code of conduct</h1>
          <div className="buyer">
            <h4>Buyer</h4>
            <ol>
              <li>There is no provision of returning a product once it has been purchased</li>
              <li>There is no provision of canceling your order once you have placed it</li>
              <li>Please note that we do not provide any warranty on the product as we are broke, warranty can only be provided by the seller</li>
            </ol>
          </div>
          <div className="seller">
            <h4>Seller</h4>
            <ol>
              <li>If there is a complaint against you about the quality of your product and it turns out to be true then you will be banned from displaying your products on our website</li>
              <li>All charges of warranty and delivery are to be taken up by the seller on thier products</li>
            </ol>
          </div>
        </div>
      </main>
      <footer>
      ©️owned by neeraj and Yousuf  
      </footer>
    </> : <Error type={error}/>
  )
}

export default LandingPage;
