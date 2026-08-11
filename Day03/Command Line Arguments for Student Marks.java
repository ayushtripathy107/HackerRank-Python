class StudentResult {
    public static void main(String[] args) {
        // Ensure the user provided exactly 4 arguments
        if (args.length < 4) {
            System.out.println("Usage: java StudentResult <Name> <Mark1> <Mark2> <Mark3>");
            return;
        }

        // Read the name argument
        String name = args[0];
        
        // Convert the string arguments to numbers (integers)
        int mark1 = Integer.parseInt(args[1]);
        int mark2 = Integer.parseInt(args[2]);
        int mark3 = Integer.parseInt(args[3]);

        // Calculate total and average
        int total = mark1 + mark2 + mark3;
        double average = total / 3.0;

        // Display results
        System.out.println("Student Name: " + name);
        System.out.println("Total Marks: " + total);
        System.out.println("Average: " + average);

        // Determine Pass/Fail
        if (average >= 40) {
            System.out.println("Result: Pass");
        } else {
            System.out.println("Result: Fail");
        }
    }
}
