class ehPrimo {
    private static final int N = 1000;
    private static final int N_THREADS = 12; // Limite da minha máquina

    public static void main(String[] args) {
        FilaTarefas pool = new FilaTarefas(N_THREADS);

        for (int i = 1; i <= N; i++) {
            final long numberToCheck = i;
            Runnable primeTask = () -> {
                if (ehPrimo(numberToCheck)) {
                    System.out.println(Thread.currentThread().getName() + " found prime: " + numberToCheck);
                }
            };
            pool.execute(primeTask);
        }

        pool.shutdown();
        System.out.println("Terminated. Total prime numbers found: " + primeCount);
    }

    static int primeCount = 0;

    static boolean ehPrimo(long n) {
        if (n <= 1) return false;
        if (n == 2) {
            incrementPrimeCount();
            return true;
        }
        if (n % 2 == 0) return false;

        for (long i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }

        incrementPrimeCount();
        return true;
    }

    static void incrementPrimeCount() {
        synchronized (ehPrimo.class) {
            primeCount++;
        }
    }
}
