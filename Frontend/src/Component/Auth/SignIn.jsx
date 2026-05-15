import React from "react"
import doSignIn from "../../../../Backend"
import { useNavigate } from "react-router"
function SignIn() {
  const [ErrorMessage, setErrorMessage] = React.useState(null)
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
    const loginData = await doSignIn(userType, email, password)
    if (loginData.successful) {
    navigate(userType == "Buyer" ? "/products" : userType == "Seller" ? "/dashboard": "/admin" )}
    else {
      setErrorMessage(loginData.errorMessage ? (loginData.errorCode === 400 ? `Your login credentials are wrong `: loginData.errorMessage)  : "We unable to login you right now because of some technical problem")
    }
  }
  return (<>
      <h1>Sign In</h1>
      <p>{ErrorMessage}</p>
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
  </>)
}

export default SignIn;
