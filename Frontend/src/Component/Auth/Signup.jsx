import React from "react"
import doSignUp from "../../../../Backend"
import { useNavigate } from "react-router"
function SignIn() {
  const [errorMessage, setErrorMessage] = React.useState(null)
  const navigate = useNavigate()
  const [userType, setUserType] = React.useState("Buyer")
  async function handleSignIn(formData) {
    setErrorMessage(null)
    if (FormData.get("cancel")) {
      navigate("/")
      return
    }
    const email = formData.get("email")
    const password = formData.get("password")
    const signupData = await doSignUp(userType, email, password)
    if (signupData.successful) {navigate(userType == "Buyer" ? "/products" : userType == "Seller" ? "/dashboard": "/admin" )}
    else {setErrorMessage(signupData.errorMessage ? signupData.errorMessage : "We are unable to login you right now")}
    
  }
  return (<>
      <h1>Sign In</h1>
      <p>{errorMessage}</p>
      <button onClick={() => setUserType("Buyer")}>Buyer</button>
      <button onClick={() => setUserType("Seller")}>Seller</button>
      <button onClick={() => setUserType("Admin")}>Admin</button>
      <form action={handleSignIn}>
        <label for="email">email</label>
        <input type="email" id="email" name="email" placeholder="123coder@gmail.com" />
        <label for="password">password</label>
        <input type="password" id="password" name="password" placeholder="12345" minLength={6} />
        <button name="submit">Submit</button>
        <button name="cancel">Cancel</button>
      </form>
      <p>Do not have an account ? </p>
  </>)
}

export default SignIn;