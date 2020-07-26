import React from 'react';

const Food = ({name, image}) => {
  return(
    <div>
      <h2>I love {name}</h2>
      <img src = {image} alt = {name}/> 
    </div>
  );
}

const FoodILike = [
  {
    id: 1,
    name: "Kimchi", 
    image: "https://www.bgw.kr/wp-content/uploads/2019/12/%EC%88%98%EC%9E%85%EA%B9%80%EC%B9%98.png"
  },
  {
    id: 2,
    name: "Mara",
    image: "https://m.atemshop.com/web/product/big/201907/8a504eee7e966a863c53316af4b41c8d.jpg"
  },
  {
    id: 3,
    name: "Ice Cream",
    image:"https://lh3.googleusercontent.com/proxy/5lAVs1uPU4xZhHlvfLzgpu9jGCnHKr_olmNFzW-2chuGqd0SroRvPQ9yxD28_YQjpk87WseR2GQ98XE6krCdxI8rO4JnwJJlj4AzUxJuBzAX"
  }
]

const App = () => {
  return <div>
          {FoodILike.map(dish => <Food key = {dish.id} name = {dish.name} image = {dish.image}/>)}
         </div>;
}

export default App;
