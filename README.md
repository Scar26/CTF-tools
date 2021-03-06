# CTF-tools
A collection of exploits or general scripts that often come in handy during CTFs

- `Sherlock`: OSINT tool used to find online presence connected to a particular username. **Credits : https://github.com/sherlock-project/sherlock**
- `jwttool.py`: Handy script for testing jsonwebtoken vulneabilities. **Credits: https://github.com/ticarpi/jwt_tool**
- `ECBoracle`: Exploit for an ECB padding oracle, a common class of challenges in security training labs. **Credits: Me**
- `getprimes`: A collection of sieves and other algorithms for fast computation of primes. **Credits: Me + Stackoverflow**
- `weiner`: Implementation of weiner's attack on RSA. **Credits: Me**
- `pupper.jpg.php`: A php reverse shell disguised as an image. Useful for fooling MIME type checks and exploiting file upload systems. **Credits: Me**
- `diggit.py`: Automatically extracts exposed git directories in websites. **Credits: https://github.com/jrfaller/diggit**
- `MiniShell1.php`: A small shell(31 characters) which does not contain any letters or numbers. Needs to be executed via `shell_exec`. Helpful for bypassing regex checks and upload limits. **Credits: https://gist.github.com/mvisat/03592a5ab0743cd43c2aa65bf45fef21**
- `MiniShell2.php`: A slightly modified version of MiniShell2.php which also works inside `eval` statements. **Credits: Me**
- `grab.php`: A simple php file to dump incoming request queries. Useful as an Out of Band exfiltration endpoint in combination with ngrok or pagekite. **Credits: Me**
- `coppersmith.py`: A simple implementation of the functions to be used in a classic coppersmith's attack on RSA **Credits: Me**
- `LCG.py`: Simple script to break LCG (linear congruential genrator) RNG. **Credits: Unknown**
- `SQLi`: Collection of scripts for extraction of data via blind SQL injection **Credits: Me, @supra08, @sin3point14**
