import streamlit as st

def main():
    st.set_page_config(page_title="Lífslíkur AI", layout="centered")
    st.title("🤖 Lífslíka- og Heilsumatsbotn")
    st.write("Svaraðu spurningunum og fáðu heilsumat og áætlaðan lífaldur.")

    with st.form("lifslikur_form"):
        st.header("1. Líkamlegt heilbrigði")
        height = st.number_input("Hver er hæð þín í sentímetrum?", 100, 250, 175)
        weight = st.number_input("Hver er þyngd þín í kílóum?", 30, 200, 70)
        exercise = st.radio("Hreyfir þú þig að minnsta kosti 150 mínútur á viku?", ["Já", "Nei"])
        vegetables = st.radio("Borðar þú grænmeti og ávexti daglega?", ["Já", "Nei"])
        smoking = st.selectbox("Reykir þú eða hefur reykt áður?", ["Aldrei", "Reykti áður", "Reykir núna"])
        alcohol = st.selectbox("Drekkur þú áfengi?", ["Aldrei", "Stundum", "Vikulega", "Daglega"])
        checkups = st.radio("Ferðu reglulega í læknisskoðun?", ["Já", "Nei"])

        st.header("2. Geðheilsa og félagsleg tengsl")
        loneliness = st.selectbox("Finnur þú til félagslegrar einangrunar?", ["Aldrei", "Stundum", "Oft"])
        relationships = st.radio("Áttu nán sambönd (vinir/fjölskylda)?", ["Já", "Nei"])
        stress = st.selectbox("Finnur þú reglulega fyrir streitu?", ["Aldrei", "Stundum", "Oft"])
        happiness = st.selectbox("Hversu oft hlærðu/hugsar jákvætt?", ["Daglega", "Stundum", "Sjaldan"])
        mental_history = st.radio("Hefur þú greinst með geðrænan vanda?", ["Já", "Nei"])

        st.header("3. Svefn")
        sleep_hours = st.slider("Hversu margar klukkustundir sefur þú á nóttu?", 3, 12, 7)
        sleep_quality = st.radio("Vaknar þú úthvíld/ur flesta morgna?", ["Já", "Nei"])
        sleep_routine = st.radio("Ferðu að sofa á svipuðum tíma á kvöldin?", ["Já", "Nei"])

        st.header("4. Umhverfi og fjárhagur")
        health_access = st.radio("Hefur þú greiðan aðgang að heilbrigðisþjónustu?", ["Já", "Nei"])
        income = st.selectbox("Hver eru árslaun þín?", ["Undir 4M", "4-8M", "8M+"])
        education = st.selectbox("Hvaða menntun hefur þú lokið?", ["Grunnskóli", "Framhaldsskóli", "Háskóli"])
        pension = st.radio("Ertu fjárhagslega örugg/ur?", ["Já", "Nei"])

        st.header("5. Erfðir og ættarsaga")
        heart_disease = st.radio("Eru hjartasjúkdómar í fjölskyldunni?", ["Já", "Nei"])
        cancer_family = st.radio("Er krabbamein algengt í fjölskyldunni?", ["Já", "Nei"])
        mental_family = st.radio("Eru geðsjúkdómar í fjölskyldunni?", ["Já", "Nei"])
        parent_age = st.slider("Hversu gamlir urðu foreldrar þínir að meðaltali?", 50, 105, 75)

        st.header("6. Lífsviðhorf og venjur")
        diet = st.selectbox("Hvernig myndirðu lýsa mataræði þínu?", ["Frábært", "Ásættanlegt", "Slæmt"])
        stress_management = st.radio("Reynir þú að stýra streitu meðvitað?", ["Já", "Nei"])
        novelty = st.radio("Gerir þú eitthvað nýtt reglulega?", ["Já", "Nei"])
        spirituality = st.radio("Ertu trúarleg/ur eða andlega sinnaður?", ["Já", "Nei"])
        purpose = st.radio("Hefur þú skýr lífsmarkmið eða tilgang?", ["Já", "Nei"])

        submitted = st.form_submit_button("Reikna lífslíkur")

    if submitted:
        score = 0

        if exercise == "Já": score += 6
        if vegetables == "Já": score += 4
        if smoking == "Aldrei": score += 5
        if alcohol in ["Aldrei", "Stundum"]: score += 3
        if checkups == "Já": score += 3
        if loneliness == "Aldrei": score += 3
        if relationships == "Já": score += 3
        if stress == "Aldrei": score += 3
        if happiness == "Daglega": score += 3
        if mental_history == "Nei": score += 3
        if 7 <= sleep_hours <= 9: score += 4
        if sleep_quality == "Já": score += 2
        if sleep_routine == "Já": score += 2
        if health_access == "Já": score += 2
        if income == "8M+": score += 2
        if education == "Háskóli": score += 2
        if pension == "Já": score += 2
        if diet == "Frábært": score += 4
        if stress_management == "Já": score += 3
        if novelty == "Já": score += 2
        if spirituality == "Já": score += 1
        if purpose == "Já": score += 3

        health_score = min(score * 2, 100)
        base_life = 72
        adj = (health_score - 50) // 3
        fam_adj = (parent_age - 72) // 3
        life_expectancy = max(40, min(base_life + adj + fam_adj, 105))

        st.success(f"Áætlaður lífaldur: {life_expectancy} ár")
        st.info(f"Heilsuvísitala þín: {health_score} / 100")

if __name__ == "__main__":
    main()
Uppfæri í rétta Streamlit útgáfu með vefviðmóti
