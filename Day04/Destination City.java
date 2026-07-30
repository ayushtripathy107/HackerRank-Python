class Solution {
    public String destCity(List<List<String>> paths) {
        Set<String> starts = new HashSet<>();
        for (List<String> p : paths) {
            starts.add(p.get(0));
        }
        for (List<String> p : paths) {
            String dest = p.get(1);
            if (!starts.contains(dest)) {
                return dest;
            }
        }
        return "";
    }
}
