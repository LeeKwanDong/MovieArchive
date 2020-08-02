import React from 'react';
import PropTypes from 'prop-types';

const Food = ({name, image, rating}) => {
  return(
    <div>
      <h2>I love {name}</h2>
      <h4>{rating}/5.0</h4>
      <img src = {image} alt = {name}/> 
    </div>
  );
}

const FoodILike = [
  {
    id: 1,
    name: "Kimchi", 
    image: "https://www.bgw.kr/wp-content/uploads/2019/12/%EC%88%98%EC%9E%85%EA%B9%80%EC%B9%98.png",
    rating: 5
  },
  {
    id: 2,
    name: "Mara",
    image: "https://m.atemshop.com/web/product/big/201907/8a504eee7e966a863c53316af4b41c8d.jpg",
    rating: 5
  },
  {
    id: 3,
    name: "Ice Cream",
    image:"https://pds.joins.com/news/component/htmlphoto_mmdata/201909/19/a971871a-4939-4470-a559-34cb75bd6606.jpg",
    rating: 5
  }
]

const App = () => {
  return <div>
          {FoodILike.map(dish => <Food key = {dish.id} name = {dish.name} image = {dish.image} rating={dish.rating}/>)}
         </div>;
}

Food.propTypes = {
 name: PropTypes.string.isRequired,
 image: PropTypes.string.isRequired,
 rating: PropTypes.number.isRequired
};

export default App;
