# Script vidéo - SPEC-3

## Alignement avec `New_training_content.md`

"Il n'y a pas de section `Script —` dédiée à cet exercice. Ce script est aligné sur l'exercice Hands On `Spec-Code Alignment & Gap Analysis` et sur le principe du module : utiliser l'IA pour vérifier la cohérence entre specification, design et implementation."

## Concept couvert

"Ce Hands On illustre l'alignement Specification-Code. Quand l'IA génère ou modifie du code, il faut vérifier que l'implémentation reste alignée avec l'intention fonctionnelle."

"La specification n'est pas un document figé. Elle sert de référence, mais elle peut aussi révéler ses propres manques quand on la compare au code."

"C'est une compétence essentielle dans un workflow agentique : l'agent peut produire vite, mais cette vitesse augmente aussi le risque de divergence silencieuse. Le code peut fonctionner, mais ne pas faire exactement ce qui était demandé. À l'inverse, le code peut révéler des comportements qui auraient dû être documentés."

"L'objectif pédagogique est donc d'apprendre à utiliser Copilot comme assistant de revue croisée. Il ne remplace pas l'expertise métier, mais il aide à repérer systématiquement les différences entre intention et réalisation."

## Mise en situation

"Nous avons deux artefacts : `spec.md`, qui décrit le comportement attendu, et `app.py`, qui contient une implementation Flask. Le travail consiste à demander à Copilot de comparer les deux et de faire ressortir les écarts."

"À l'écran, montrez d'abord la specification. Elle contient les endpoints attendus, les validations et quelques limitations connues. Ensuite, ouvrez `app.py` et montrez que le code contient les routes et les règles réelles."

"Expliquez que l'exercice ne consiste pas à juger uniquement le code. Il consiste à identifier la source de vérité : parfois la specification est bonne et le code doit changer ; parfois le code est raisonnable mais la specification n'a pas été assez précise."

## Démonstration du début

"J'ouvre `spec.md` et `app.py`, puis je les fournis à Copilot. Je demande une comparaison structurée : endpoints manquants, mauvais codes HTTP, validations absentes, champs non documentés."

"Ensuite, je demande à Copilot d'identifier les comportements présents dans le code mais absents de la specification : valeurs par défaut, cas d'erreur, comportements implicites."

"Montrez comment formuler la demande pour obtenir un rapport exploitable. Par exemple : 'Classify each finding as code issue, spec issue, ambiguity, or missing edge case'. Cette classification oblige Copilot à structurer son analyse."

"Ensuite, prenez un exemple de finding et discutez-le. Si la specification ne dit pas comment combiner deux filtres, le code peut choisir AND par défaut. Est-ce un bug ? Pas forcément. Mais c'est une ambiguïté à documenter."

"Montrez que Copilot peut aussi proposer des reformulations. Cela permet de transformer directement une remarque en amélioration de `spec-v2.md`."

## Consignes pour l'exercice

"Votre livrable est double : un `alignment-report.md` qui liste les écarts, et un `spec-v2.md` qui améliore la specification."

"Dans `alignment-report.md`, ne listez pas seulement les problèmes. Ajoutez une décision : code to fix, spec to fix, or open question. Cette décision est la partie humaine de l'exercice."

"Dans `spec-v2.md`, corrigez au moins deux sections. L'objectif est d'avoir une specification plus claire après l'analyse qu'avant."

## Points d'attention à montrer à l'écran

"Montrez la différence entre un écart bloquant et une simple amélioration. Un mauvais status code peut être un bug. Une règle de filtre non documentée peut être une lacune de specification."

"Montrez aussi que Copilot peut halluciner un écart s'il lit trop vite. Il faut donc vérifier ses conclusions dans le code et dans la specification."

## Conclusion

"L'alignement spec-code est un contrôle qualité très puissant. Il permet de fermer la boucle entre ce qui était demandé et ce qui a été construit."

"Le réflexe à retenir : après génération ou modification par IA, comparez toujours le résultat avec la specification initiale."
