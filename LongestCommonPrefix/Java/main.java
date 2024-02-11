public class main {

    public static String solveProblem(String[] strs)
    {
        if(strs.length == 0)
        {
            return "No Data Found";
        }

        String currentPrefix = strs[0];

        for(int i = 1; i <= strs.length - 1; i++)
        {
            String prefix = "";
            int characterRange = currentPrefix.length();

            if(characterRange > strs[i].length())
                characterRange = strs[i].length();
            
            for(int j = 0; j <= characterRange - 1; j++)
            {
                if(currentPrefix.charAt(j) == strs[i].charAt(j))
                    prefix = prefix + strs[i].charAt(j);
            }

            currentPrefix = prefix;
        }

        return currentPrefix;
    }

    public static void main(String[] args) {

        String[] input = new String[]{};
        System.out.println(solveProblem(input));

        input = new String[]{"flower","flow","flight"};
        System.out.println(solveProblem(input));

        input = new String[]{"aaabcdea","aaabfredsasdfg","aaabc"};
        System.out.println(solveProblem(input));

        input = new String[]{"car","can","cat"};
        System.out.println(solveProblem(input));

        input = new String[]{"dog","racecar","car"};
        System.out.println(solveProblem(input));

        input = new String[]{"bats","batter","barn"};
        System.out.println(solveProblem(input));
    }
}
