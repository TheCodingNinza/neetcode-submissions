class Solution {
    class Car{
        int position;
        int speed;

        public Car(int position, int speed){
            this.position = position;
            this.speed = speed;
        } 
        @Override
        public String toString() {
            return "Car{" +
                "position=" + position +
                ", speed=" + speed +
                '}';
        }
    }
    public int carFleet(int target, int[] position, int[] speed) {
        List<Car> cars = new ArrayList<>();
        for(int i=0 ; i < position.length; i++){
            cars.add(new Car(position[i], speed[i]));
        }
        Collections.sort(cars, (p1, p2) -> p1.position - p2.position);
        System.out.println(cars);
        int numberOfFleets = 0;
        Stack<Double> stk = new Stack<>();
        stk.push(((double)target - (double)cars.get(cars.size()-1).position) / (double)cars.get(cars.size()-1).speed);
        for(int i=cars.size()-2; i >= 0; i--){
            Car currCar = cars.get(i);
            double carAtTopTime = stk.peek();
            double currCarTime = ((double)target - (double)currCar.position) / (double)currCar.speed;
            if(currCarTime > carAtTopTime){
                stk.push(currCarTime);
            }
        }
        return stk.size();
    }
}
