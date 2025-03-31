# AI BOT FOR PREDICTING LIFE EXPECTANCY AND HEALTH SCORE
# Using principles from Public Health, Sociology, Psychology, Medicine, Economics, etc.

import random

class LifeExpectancyAIBot:
    def __init__(self):
        self.questions = self._generate_questions()
        self.responses = {}

    def _generate_questions(self):
        return {
            # Physical Health
            "height": "Hver er hæð þín í sentímetrum?",
            "weight": "Hver er þyngd þín í kílóum?",
            "exercise": "Hreyfir þú þig að minnsta kosti 150 mínútur á viku? (já/nei)",
            "vegetables": "Borðar þú grænmeti og ávexti daglega? (já/nei)",
            "smoking": "Reykir þú eða hefur reykt áður? (aldrei/reykti/reyki enn)",
            "alcohol": "Drekkur þú áfengi? (aldrei/stundum/vikulega/daglega)",
            "checkups": "Ferðu reglulega í læknisskoðun (árlega)? (já/nei)",

            # Mental Health & Social
            "loneliness": "Finnur þú til félagslegrar einangrunar? (aldrei/stundum/oft)",
            "relationships": "Áttu nán sambönd (vinir/fjölskylda)? (já/nei)",
            "stress": "Finnur þú reglulega fyrir streitu? (aldrei/stundum/oft)",
            "happiness": "Hversu oft hlærðu/hugsar jákvætt? (daglega/stundum/sjaldan)",
            "mental_history": "Hefur þú greinst með geðrænan vanda? (já/nei)",

            # Sleep
            "sleep_hours": "Hversu margar klukkustundir sefur þú að meðaltali á nóttu?",
            "sleep_quality": "Vaknar þú úthvíld/ur flesta morgna? (já/nei)",
            "sleep_routine": "Ferðu alltaf að sofa á svipuðum tíma? (já/nei)",

            # Environmental & Economic
            "residence": "Hvar býrðu? (borg/smábær/sveit)",
            "health_access": "Hefur þú greiðan aðgang að heilbrigðisþjónustu? (já/nei)",
            "income": "Hver eru árslaun þín? (undir 4M/4-8M/8M+)",
            "education": "Hvaða menntun hefur þú lokið? (grunnskóli/framhaldsskóli/háskóli)",
            "employment": "Ertu í vinnu? (já/nei/eftirlaun)",
            "pension": "Ertu fjárhagslega örugg/ur? (já/nei)",

            # Family History
            "heart_disease": "Eru hjartasjúkdómar í fjölskyldunni? (já/nei)",
            "cancer_family": "Hefur einhver í fjölskyldunni fengið krabbamein? (já/nei)",
            "mental_family": "Eru geðsjúkdómar í fjölskyldunni? (já/nei)",
            "parent_age": "Hversu gamlir urðu foreldrar þínir (að meðaltali)?",

            # Lifestyle
            "diet": "Hvernig myndirðu lýsa mataræði þínu? (frábært/ásættanlegt/slæmt)",
            "stress_management": "Reynir þú að stýra streitu (t.d. með hugleiðslu)? (já/nei)",
            "novelty": "Gerir þú eitthvað nýtt/mismunandi reglulega? (já/nei)",
            "spirituality": "Ertu andlega eða trúarlega sinnaður? (já/nei)",
            "purpose": "Hefur þú tilgang eða lífsmarkmið? (já/nei)"
        }

    def collect_responses(self):
        print("\n--- Spurningalisti AI Bots ---")
        for key, question in self.questions.items():
            answer = input(f"{question}\n> ")
            self.responses[key] = answer.strip().lower()

    def calculate_health_score(self):
        score = 0

        # Sample scoring logic, can be deeply improved per research
        if self.responses.get("exercise") == "já": score += 6
        if self.responses.get("vegetables") == "já": score += 4
        if self.responses.get("smoking") == "aldrei": score += 5
        if self.responses.get("alcohol") in ["aldrei", "stundum"]: score += 3
        if self.responses.get("checkups") == "já": score += 3

        if self.responses.get("loneliness") == "aldrei": score += 3
        if self.responses.get("relationships") == "já": score += 3
        if self.responses.get("stress") == "aldrei": score += 3
        if self.responses.get("happiness") == "daglega": score += 3
        if self.responses.get("mental_history") == "nei": score += 3

        if self.responses.get("sleep_hours") and 7 <= int(self.responses["sleep_hours"]) <= 9:
            score += 4
        if self.responses.get("sleep_quality") == "já": score += 2
        if self.responses.get("sleep_routine") == "já": score += 2

        if self.responses.get("health_access") == "já": score += 2
        if self.responses.get("income") == "8m+": score += 2
        if self.responses.get("education") == "háskóli": score += 2
        if self.responses.get("pension") == "já": score += 2

        if self.responses.get("diet") == "frábært": score += 4
        if self.responses.get("stress_management") == "já": score += 3
        if self.responses.get("novelty") == "já": score += 2
        if self.responses.get("spirituality") == "já": score += 1
        if self.responses.get("purpose") == "já": score += 3

        return min(score * 2, 100)  # Scale to 100

    def predict_life_expectancy(self):
        base = 72  # Base life expectancy
        score = self.calculate_health_score()
        adjustment = (score - 50) // 3  # For every 3 points above/below 50, add/subtract 1 year

        family_adjustment = 0
        try:
            parent_avg_age = int(self.responses.get("parent_age", "72"))
            family_adjustment = (parent_avg_age - 72) // 3
        except ValueError:
            pass

        total_life_expectancy = base + adjustment + family_adjustment
        return max(40, min(total_life_expectancy, 105))  # Clamp value

    def run(self):
        self.collect_responses()
        health_score = self.calculate_health_score()
        life_expectancy = self.predict_life_expectancy()

        print("\n--- Niðurstöður ---")
        print(f"Heilsuvísitala þín: {health_score}/100")
        print(f"Áætlaður lífaldur: {life_expectancy} ár")


# Kalla á líkanið
aibot = LifeExpectancyAIBot()
aibot.run()
