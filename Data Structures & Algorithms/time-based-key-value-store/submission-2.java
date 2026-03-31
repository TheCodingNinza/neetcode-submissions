class TimeMap {
    class Pair{
        int index;
        String value;
        public Pair(int index, String value){
            this.index = index;
            this.value = value;
        }

    }

    private Map<String, List<Pair>> map;

    public TimeMap() {
        this.map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        this.map.computeIfAbsent(key, x -> new ArrayList<>()).add(new Pair(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        if(!this.map.containsKey(key)){
            return "";
        }else{
            List<Pair> list = map.get(key);
            int low = 0;
            int high = list.size() - 1;
            int foundIndex = Integer.MAX_VALUE;
            // System.out.println("size: "+list.size());
            while(low <= high){
                int mid = (low + high) / 2;
                Pair currElem = list.get(mid);
                if(currElem.index == timestamp){
                    return currElem.value;
                }else if(currElem.index < timestamp){
                    foundIndex = mid;
                    low = mid + 1;
                }else{
                    // foundIndex = mid;
                    high = mid - 1;
                }
            }
            return foundIndex != Integer.MAX_VALUE ? list.get(foundIndex).value : "";
        }
    }
}
