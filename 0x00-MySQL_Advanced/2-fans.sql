-- SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fan

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
WHERE fans IS NOT NULL
GROUP BY origin
ORDER BY nb_fans DESC;

