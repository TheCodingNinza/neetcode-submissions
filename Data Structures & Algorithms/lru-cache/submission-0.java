class LRUCache {
    private Map<Integer, Pair> map;
    private TreeMap<Integer, List<Integer>> timeMap;
    private int time;
    private int capacity;

    public LRUCache(int capacity) {
        this.map = new HashMap<>();
        this.timeMap = new TreeMap<>();
        this.time = 0;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            Pair elem = map.get(key);
            List<Integer> list = timeMap.get(elem.time);
            list.remove((Integer) key);
            if(list.size() == 0)
                this.timeMap.remove(elem.time);
            this.time++;
            this.timeMap.computeIfAbsent(this.time, x-> new LinkedList<>()).add(key);
            elem.time = this.time;
            return elem.value;
        }else{
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if(this.map.containsKey(key)){
            Pair elem = map.get(key);
            List<Integer> list = timeMap.get(elem.time);
            list.remove((Integer) key);
            if(list.size() == 0)
                this.timeMap.remove(elem.time);
            this.time++;
            this.timeMap.computeIfAbsent(this.time, x-> new LinkedList<>()).add(key);
            elem.time = this.time;
            elem.value = value;
        }else{
            if(this.map.size() < this.capacity ){
                this.time++;
                Pair elem = new Pair(value, this.time);
                this.map.put(key, elem);
                this.timeMap.computeIfAbsent(this.time, x-> new LinkedList<>()).add(key);
            }else{
                int keyToRemove = this.timeMap.firstEntry().getValue().get(0);
                this.timeMap.firstEntry().getValue().remove(0);
                if(this.timeMap.firstEntry().getValue().size() == 0)
                    this.timeMap.pollFirstEntry();
                this.map.remove((Integer) keyToRemove);
                this.time++;
                Pair elem = new Pair(value, this.time);
                this.map.put(key, elem);
                this.timeMap.computeIfAbsent(this.time, x-> new LinkedList<>()).add(key);
            }
        }
    }

    class Pair {
        int value;
        int time;
        public Pair(int value, int time){
            this.value = value;
            this.time = time;
        }
    }
}
