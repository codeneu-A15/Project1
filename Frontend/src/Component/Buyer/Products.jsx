import getAllProducts from "../../../../Backend"
import {useNavigate} from "react-router"
import React from "react"
function Products() {
  const navigate = useNavigate()
  const [products, setProducts] = React.useState([])
  React.useEffect(() => {
    async function gettingProducts() {
      const product = await getAllProducts()
      setProducts(product)
    }
    gettingProducts()
  }, [])
  const productsJSX = products.map(item => {<button onClick={() => {navigate(`/product/${item.id}`)}}>
  <h1>{item.title}</h1>
  <img src={item.url} />
  <p>{item.shortdesc}</p>
  <p>{item.category.map((category, index) => <h3>{`{${index + 1}`}{category}</h3>)}</p>
  </button>})
  return (
    <>
    <header>
      <img src="" />
    </header>
    <main>
    {productsJSX}
    </main>
    <footer>
      ©️ owned by Neeraj Mishra and Yousuf
    </footer>
    </>
  )
}

export default Products;
