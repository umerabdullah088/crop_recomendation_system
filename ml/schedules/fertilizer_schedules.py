"""
Predefined Fertilizer Schedules
================================

Phase 1 of the agricultural decision-support system.

Purpose:
    Store source-based fertilizer/nutrient application stages for the
    crops supported by the crop recommendation model.

Important:
    These are predefined advisory schedules, NOT dynamic prescriptions.

    Actual fertilizer dose can depend on:
        - soil test
        - crop variety
        - region
        - irrigation condition
        - crop age
        - expected yield
        - local agricultural recommendations

    The system should therefore use these schedules as a planning layer.
    Later, field/soil data can be used to make recommendations dynamic.

Timing conventions:
    - days_after_planting: relative to planting/transplanting
    - days_after_sowing: relative to sowing
    - weeks_after_planting: relative to planting
    - months_after_planting: relative to planting
    - stage: crop growth stage
    - seasonal: calendar/season-based application

Nutrient notation:
    N   = Nitrogen
    P   = Phosphorus / P2O5
    K   = Potassium / K2O

Sources used as the basis for the schedule:
    - ICAR agricultural advisories
    - TNAU Agritech crop nutrient-management recommendations

This file intentionally avoids pretending that one fertilizer rate is
universally correct for every farm.
"""


# ============================================================
# 1. RICE
# ============================================================

RICE_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "basal",
        "days_after_planting": 0,
        "recommendation": "Apply basal portion of nitrogen with full phosphorus and the basal portion of potassium.",
        "nutrients": ["N", "P", "K"],
        "notes": "Exact dose should follow soil-test/local recommendation."
    },
    {
        "stage": "Active Tillering",
        "timing_type": "days_after_planting",
        "days_after_planting": 35,
        "recommendation": "Apply the next nitrogen split.",
        "nutrients": ["N"],
        "notes": "Timing varies with crop duration."
    },
    {
        "stage": "Panicle Initiation",
        "timing_type": "crop_stage",
        "recommendation": "Apply remaining nitrogen and the remaining potassium split.",
        "nutrients": ["N", "K"],
        "notes": "Use crop-stage observation rather than a fixed calendar date."
    },
]


# ============================================================
# 2. MAIZE
# ============================================================

MAIZE_SCHEDULE = [
    {
        "stage": "Sowing",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply basal phosphorus, potassium and part of nitrogen.",
        "nutrients": ["N", "P", "K"],
        "notes": "ICAR advisory examples use full P and K with part of N at sowing."
    },
    {
        "stage": "Early Growth",
        "timing_type": "days_after_sowing",
        "days_after_sowing": 30,
        "recommendation": "Apply the next nitrogen split.",
        "nutrients": ["N"],
        "notes": "Approximate stage; adjust according to local recommendation."
    },
    {
        "stage": "Ear Formation",
        "timing_type": "crop_stage",
        "recommendation": "Apply the final nitrogen split.",
        "nutrients": ["N"],
        "notes": "Crop-stage based application is preferred."
    },
]


# ============================================================
# 3. CHICKPEA
# ============================================================

CHICKPEA_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply the recommended basal NPK dose before/at sowing.",
        "nutrients": ["N", "P", "K"],
        "notes": "Pulses generally receive much of their fertilizer as basal application."
    },
    {
        "stage": "Flowering",
        "timing_type": "crop_stage",
        "recommendation": "Monitor crop nutrient status and apply supplemental nutrition only when recommended.",
        "nutrients": [],
        "notes": "Avoid creating a universal top-dressing dose without soil/crop context."
    },
]


# ============================================================
# 4. KIDNEY BEANS
# ============================================================

KIDNEYBEANS_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply recommended NPK as basal fertilizer.",
        "nutrients": ["N", "P", "K"],
        "notes": "Rate depends on soil fertility and production region."
    },
    {
        "stage": "Vegetative Growth",
        "timing_type": "crop_stage",
        "recommendation": "Monitor nutrient status and apply additional nutrition if locally recommended.",
        "nutrients": ["N"],
        "notes": "Do not use a fixed universal dose."
    },
]


# ============================================================
# 5. PIGEONPEA
# ============================================================

PIGEONPEAS_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply recommended basal nitrogen, phosphorus and potassium.",
        "nutrients": ["N", "P", "K"],
        "notes": "A documented example uses approximately 20:40:20 kg/ha N:P:K, but local recommendations should take precedence."
    },
    {
        "stage": "Vegetative / Branching",
        "timing_type": "crop_stage",
        "recommendation": "Monitor crop nutrient condition.",
        "nutrients": [],
        "notes": "Additional fertilizer depends on soil and local recommendation."
    },
]


# ============================================================
# 6. MOTHBEANS
# ============================================================

MOTHBEANS_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply recommended basal fertilizer before or at sowing.",
        "nutrients": ["N", "P", "K"],
        "notes": "Use soil-test/local pulse recommendation."
    },
    {
        "stage": "Flowering",
        "timing_type": "crop_stage",
        "recommendation": "Monitor nutrient status during flowering.",
        "nutrients": [],
        "notes": "Avoid prescribing a universal top-dressing rate."
    },
]


# ============================================================
# 7. MUNGBEAN / GREENGRAM
# ============================================================

MUNGBEAN_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply recommended NPKS fertilizer as basal.",
        "nutrients": ["N", "P", "K", "S"],
        "notes": "TNAU gives a blanket pulse recommendation with the entire NPKS dose applied basally."
    },
    {
        "stage": "Flowering",
        "timing_type": "crop_stage",
        "recommendation": "Monitor crop condition and provide supplemental nutrition only where recommended.",
        "nutrients": [],
        "notes": "Foliar nutrient practices are separate from basal fertilizer."
    },
]


# ============================================================
# 8. BLACKGRAM / URDBEAN
# ============================================================

BLACKGRAM_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply the recommended NPKS dose as basal fertilizer.",
        "nutrients": ["N", "P", "K", "S"],
        "notes": "TNAU recommends applying the entire NPKS quantity basally."
    },
    {
        "stage": "30 DAS",
        "timing_type": "days_after_sowing",
        "days_after_sowing": 30,
        "recommendation": "Optional foliar nitrogen where recommended for yield improvement.",
        "nutrients": ["N"],
        "notes": "TNAU documents 1% urea foliar spray at 30 and 45 DAS; this is foliar nutrition, not soil fertilizer."
    },
    {
        "stage": "45 DAS",
        "timing_type": "days_after_sowing",
        "days_after_sowing": 45,
        "recommendation": "Optional foliar nitrogen where recommended.",
        "nutrients": ["N"],
        "notes": "Apply only according to the applicable agricultural recommendation."
    },
]


# ============================================================
# 9. LENTIL
# ============================================================

LENTIL_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply recommended basal NPK fertilizer.",
        "nutrients": ["N", "P", "K"],
        "notes": "Dose depends on soil fertility and local recommendation."
    },
    {
        "stage": "Vegetative Growth",
        "timing_type": "crop_stage",
        "recommendation": "Monitor nutrient status.",
        "nutrients": [],
        "notes": "Additional fertilizer should be based on local recommendation."
    },
]


# ============================================================
# 10. POMEGRANATE
# ============================================================

POMEGRANATE_SCHEDULE = [
    {
        "stage": "First Year",
        "timing_type": "tree_age",
        "tree_age_years": 1,
        "recommendation": "Apply annual manure and fertilizer requirement according to tree age.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU gives age-specific per-plant recommendations."
    },
    {
        "stage": "Second to Fifth Year",
        "timing_type": "tree_age",
        "tree_age_years": "2-5",
        "recommendation": "Increase annual fertilizer/manure dose according to tree age.",
        "nutrients": ["N", "P", "K"],
        "notes": "Use age-specific recommendation."
    },
    {
        "stage": "Sixth Year Onwards",
        "timing_type": "tree_age",
        "tree_age_years": "6+",
        "recommendation": "Use mature-tree fertilizer requirement.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU provides a higher mature-tree requirement."
    },
]


# ============================================================
# 11. BANANA
# ============================================================

BANANA_SCHEDULE = [
    {
        "stage": "Establishment",
        "timing_type": "weeks_after_planting",
        "weeks_after_planting": "9-18",
        "recommendation": "Apply the first major fertigation/application portion.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU fertigation schedule allocates nutrient proportions across this stage."
    },
    {
        "stage": "Vegetative Growth",
        "timing_type": "weeks_after_planting",
        "weeks_after_planting": "19-30",
        "recommendation": "Apply the major vegetative nutrient portion.",
        "nutrients": ["N", "K"],
        "notes": "TNAU allocates a larger share of N and K during this period."
    },
    {
        "stage": "Shooting",
        "timing_type": "weeks_after_planting",
        "weeks_after_planting": "31-42",
        "recommendation": "Continue nutrient application with emphasis on crop-stage requirements.",
        "nutrients": ["N", "K"],
        "notes": "Follow the applicable banana production system."
    },
    {
        "stage": "Development / Harvesting",
        "timing_type": "weeks_after_planting",
        "weeks_after_planting": "43-45",
        "recommendation": "Apply final potassium portion where applicable.",
        "nutrients": ["K"],
        "notes": "TNAU schedule assigns the remaining K during this period."
    },
]


# ============================================================
# 12. MANGO
# ============================================================

MANGO_SCHEDULE = [
    {
        "stage": "After Harvest",
        "timing_type": "crop_stage",
        "recommendation": "Apply the post-harvest nutrient portion.",
        "nutrients": ["N", "P", "K"],
        "notes": "For high-density bearing trees, TNAU distributes nutrients by stage."
    },
    {
        "stage": "Pre-flowering",
        "timing_type": "crop_stage",
        "recommendation": "Apply the pre-flowering nutrient portion.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU gives stage-wise nutrient percentages."
    },
    {
        "stage": "Flowering to Fruit Set",
        "timing_type": "crop_stage",
        "recommendation": "Apply flowering/fruit-set nutrient portion.",
        "nutrients": ["N", "P", "K"],
        "notes": "Avoid applying a generic fixed dose without tree age/production context."
    },
    {
        "stage": "Fruit Development",
        "timing_type": "crop_stage",
        "recommendation": "Apply fruit-development nutrient portion.",
        "nutrients": ["N", "K"],
        "notes": "Potassium becomes particularly important in this stage."
    },
]


# ============================================================
# 13. GRAPES
# ============================================================

GRAPES_SCHEDULE = [
    {
        "stage": "Immediately After Pruning",
        "timing_type": "after_pruning",
        "recommendation": "Apply half of the recommended potash dose.",
        "nutrients": ["K"],
        "notes": "TNAU recommends half the potash after pruning."
    },
    {
        "stage": "60 Days After Pruning",
        "timing_type": "days_after_pruning",
        "days_after_pruning": 60,
        "recommendation": "Apply the remaining half of the recommended potash dose.",
        "nutrients": ["K"],
        "notes": "Timing is based on pruning rather than planting."
    },
    {
        "stage": "Before Flowering",
        "timing_type": "crop_stage",
        "recommendation": "Correct micronutrient deficiencies according to recommendation.",
        "nutrients": ["B", "Zn", "N"],
        "notes": "TNAU documents foliar nutrition before flowering."
    },
]


# ============================================================
# 14. WATERMELON
# ============================================================

WATERMELON_SCHEDULE = [
    {
        "stage": "Establishment",
        "timing_type": "crop_stage",
        "recommendation": "Begin split nutrient application/fertigation.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU uses stage-wise fertigation."
    },
    {
        "stage": "Vegetative Growth",
        "timing_type": "crop_stage",
        "recommendation": "Continue split nutrient application.",
        "nutrients": ["N", "P", "K"],
        "notes": "Adjust according to crop development."
    },
    {
        "stage": "Flower Initiation / First Picking",
        "timing_type": "crop_stage",
        "recommendation": "Continue nutrient supply during flowering and early fruit development.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU recommends split fertigation through crop stages."
    },
    {
        "stage": "Harvesting",
        "timing_type": "crop_stage",
        "recommendation": "Complete the final scheduled nutrient applications.",
        "nutrients": ["N", "P", "K"],
        "notes": "Do not apply excessive nitrogen late in the crop."
    },
]


# ============================================================
# 15. MUSKMELON
# ============================================================

MUSKMELON_SCHEDULE = [
    {
        "stage": "Establishment",
        "timing_type": "crop_stage",
        "recommendation": "Begin split NPK application.",
        "nutrients": ["N", "P", "K"],
        "notes": "Follow the applicable fertigation/local recommendation."
    },
    {
        "stage": "Vegetative Growth",
        "timing_type": "crop_stage",
        "recommendation": "Continue split NPK application.",
        "nutrients": ["N", "P", "K"],
        "notes": "Maintain balanced nutrition."
    },
    {
        "stage": "Flowering / Fruit Set",
        "timing_type": "crop_stage",
        "recommendation": "Continue stage-based nutrient application.",
        "nutrients": ["N", "P", "K"],
        "notes": "Avoid excessive nitrogen during fruit development."
    },
    {
        "stage": "Harvesting",
        "timing_type": "crop_stage",
        "recommendation": "Complete final scheduled nutrient applications.",
        "nutrients": ["K"],
        "notes": "Adjust according to production system."
    },
]


# ============================================================
# 16. APPLE
# ============================================================

APPLE_SCHEDULE = [
    {
        "stage": "Dormant / Pre-season",
        "timing_type": "seasonal",
        "recommendation": "Apply organic manure and nutrients according to tree age and soil-test recommendation.",
        "nutrients": ["N", "P", "K"],
        "notes": "Apple fertilizer requirements vary substantially with tree age and production system."
    },
    {
        "stage": "Flowering / Fruit Set",
        "timing_type": "crop_stage",
        "recommendation": "Monitor nutrient status and correct deficiencies.",
        "nutrients": ["N", "P", "K"],
        "notes": "Do not use a universal fertilizer quantity."
    },
    {
        "stage": "Fruit Development",
        "timing_type": "crop_stage",
        "recommendation": "Maintain balanced nutrition based on orchard recommendation.",
        "nutrients": ["K"],
        "notes": "Soil and leaf analysis should guide orchard nutrition."
    },
]


# ============================================================
# 17. ORANGE
# ============================================================

ORANGE_SCHEDULE = [
    {
        "stage": "Annual Basal / Soil Application",
        "timing_type": "seasonal",
        "recommendation": "Apply manure and fertilizer according to tree age and local citrus recommendation.",
        "nutrients": ["N", "P", "K"],
        "notes": "Tree age and production condition affect fertilizer requirement."
    },
    {
        "stage": "Flowering",
        "timing_type": "crop_stage",
        "recommendation": "Monitor nutrient status during flowering.",
        "nutrients": ["N", "P", "K"],
        "notes": "Use local citrus recommendation."
    },
    {
        "stage": "Fruit Development",
        "timing_type": "crop_stage",
        "recommendation": "Maintain balanced nutrition through fruit development.",
        "nutrients": ["N", "K"],
        "notes": "Avoid generic fixed rates."
    },
]


# ============================================================
# 18. PAPAYA
# ============================================================

PAPAYA_SCHEDULE = [
    {
        "stage": "Planting",
        "timing_type": "planting",
        "days_after_planting": 0,
        "recommendation": "Apply FYM as basal and establish the crop with recommended nutrition.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU recommends FYM at planting."
    },
    {
        "stage": "Third Month Onwards",
        "timing_type": "months_after_planting",
        "months_after_planting": 3,
        "repeat_every_months": 2,
        "recommendation": "Apply the recommended N, P and K quantity at bimonthly intervals.",
        "nutrients": ["N", "P", "K"],
        "notes": "Continue at bimonthly intervals according to crop condition."
    },
    {
        "stage": "Six Months",
        "timing_type": "months_after_planting",
        "months_after_planting": 6,
        "recommendation": "Repeat recommended biofertilizer application where applicable.",
        "nutrients": [],
        "notes": "Separate from chemical fertilizer."
    },
]


# ============================================================
# 19. COCONUT
# ============================================================

COCONUT_SCHEDULE = [
    {
        "stage": "Young Palm",
        "timing_type": "tree_age",
        "tree_age_years": "0-2",
        "recommendation": "Use age-specific fertilizer requirement and split applications.",
        "nutrients": ["N", "P", "K"],
        "notes": "Kerala recommendations vary with palm age and rainfed/irrigated condition."
    },
    {
        "stage": "First Seasonal Application",
        "timing_type": "seasonal",
        "season": "June-July",
        "recommendation": "Apply first half of the annual fertilizer requirement.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU recommends seasonal split application."
    },
    {
        "stage": "Second Seasonal Application",
        "timing_type": "seasonal",
        "season": "December-January",
        "recommendation": "Apply second half of the annual fertilizer requirement.",
        "nutrients": ["N", "P", "K"],
        "notes": "Use palm-age and local soil recommendations."
    },
]


# ============================================================
# 20. COTTON
# ============================================================

COTTON_SCHEDULE = [
    {
        "stage": "Basal",
        "timing_type": "sowing",
        "days_after_sowing": 0,
        "recommendation": "Apply the recommended basal phosphorus and part of nitrogen/potassium.",
        "nutrients": ["N", "P", "K"],
        "notes": "Exact split depends on cotton type and production system."
    },
    {
        "stage": "Vegetative Growth",
        "timing_type": "days_after_sowing",
        "days_after_sowing": 40,
        "recommendation": "Apply a top-dressing nitrogen/potassium portion where recommended.",
        "nutrients": ["N", "K"],
        "notes": "TNAU schedules use split application."
    },
    {
        "stage": "Square / Flowering",
        "timing_type": "crop_stage",
        "recommendation": "Apply remaining nutrient split according to cotton recommendation.",
        "nutrients": ["N", "K"],
        "notes": "Hybrid and variety-specific schedules differ."
    },
]


# ============================================================
# 21. JUTE
# ============================================================

JUTE_SCHEDULE = [
    {
        "stage": "Last Ploughing / Basal",
        "timing_type": "pre_sowing",
        "recommendation": "Apply organic manure and basal NPK.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU recommends basal nutrient application."
    },
    {
        "stage": "First Top Dressing",
        "timing_type": "days_after_sowing",
        "days_after_sowing": 22,
        "recommendation": "Apply first nitrogen top dressing after first weeding.",
        "nutrients": ["N"],
        "notes": "TNAU gives approximately 20-25 DAS."
    },
    {
        "stage": "Second Top Dressing",
        "timing_type": "days_after_sowing",
        "days_after_sowing": 38,
        "recommendation": "Apply second nitrogen top dressing after second weeding.",
        "nutrients": ["N"],
        "notes": "TNAU gives approximately 35-40 DAS."
    },
]


# ============================================================
# 22. COFFEE
# ============================================================

COFFEE_SCHEDULE = [
    {
        "stage": "Pre-blossom",
        "timing_type": "seasonal",
        "season": "March",
        "recommendation": "Apply the first seasonal nutrient dose according to coffee type and crop load.",
        "nutrients": ["N", "P", "K"],
        "notes": "TNAU coffee recommendations vary by Arabica/Robusta, age and expected crop."
    },
    {
        "stage": "Post-blossom",
        "timing_type": "seasonal",
        "season": "May",
        "recommendation": "Apply the second seasonal nutrient dose.",
        "nutrients": ["N", "P", "K"],
        "notes": "Use crop-specific recommendation."
    },
    {
        "stage": "Mid-monsoon",
        "timing_type": "seasonal",
        "season": "August",
        "recommendation": "Apply the third seasonal nutrient dose.",
        "nutrients": ["N", "P", "K"],
        "notes": "Adjust according to crop load and soil condition."
    },
    {
        "stage": "Post-monsoon",
        "timing_type": "seasonal",
        "season": "October",
        "recommendation": "Apply the fourth seasonal nutrient dose.",
        "nutrients": ["N", "P", "K"],
        "notes": "Use the applicable coffee production recommendation."
    },
]


# ============================================================
# MASTER SCHEDULE
# ============================================================

FERTILIZER_SCHEDULES = {

    "rice": RICE_SCHEDULE,

    "maize": MAIZE_SCHEDULE,

    "chickpea": CHICKPEA_SCHEDULE,

    "kidneybeans": KIDNEYBEANS_SCHEDULE,

    "pigeonpeas": PIGEONPEAS_SCHEDULE,

    "mothbeans": MOTHBEANS_SCHEDULE,

    "mungbean": MUNGBEAN_SCHEDULE,

    "blackgram": BLACKGRAM_SCHEDULE,

    "lentil": LENTIL_SCHEDULE,

    "pomegranate": POMEGRANATE_SCHEDULE,

    "banana": BANANA_SCHEDULE,

    "mango": MANGO_SCHEDULE,

    "grapes": GRAPES_SCHEDULE,

    "watermelon": WATERMELON_SCHEDULE,

    "muskmelon": MUSKMELON_SCHEDULE,

    "apple": APPLE_SCHEDULE,

    "orange": ORANGE_SCHEDULE,

    "papaya": PAPAYA_SCHEDULE,

    "coconut": COCONUT_SCHEDULE,

    "cotton": COTTON_SCHEDULE,

    "jute": JUTE_SCHEDULE,

    "coffee": COFFEE_SCHEDULE,
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_schedule(crop):
    """
    Return the predefined fertilizer schedule for a crop.

    Example:
        get_schedule("rice")
    """

    crop = crop.strip().lower()

    if crop not in FERTILIZER_SCHEDULES:
        raise ValueError(
            f"Unsupported crop: {crop}. "
            f"Available crops: {list(FERTILIZER_SCHEDULES.keys())}"
        )

    return FERTILIZER_SCHEDULES[crop]


def get_supported_crops():
    """
    Return all crops for which a predefined fertilizer schedule exists.
    """

    return list(FERTILIZER_SCHEDULES.keys())


def print_schedule(crop):
    """
    Print a crop's fertilizer schedule in a readable format.
    """

    schedule = get_schedule(crop)

    print("=" * 70)
    print(f"FERTILIZER SCHEDULE: {crop.upper()}")
    print("=" * 70)

    for index, item in enumerate(schedule, start=1):

        print(f"\n{index}. {item['stage']}")

        if "timing_type" in item:
            print(f"   Timing Type: {item['timing_type']}")

        if "days_after_planting" in item:
            print(
                f"   Days After Planting: "
                f"{item['days_after_planting']}"
            )

        if "days_after_sowing" in item:
            print(
                f"   Days After Sowing: "
                f"{item['days_after_sowing']}"
            )

        if "weeks_after_planting" in item:
            print(
                f"   Weeks After Planting: "
                f"{item['weeks_after_planting']}"
            )

        if "months_after_planting" in item:
            print(
                f"   Months After Planting: "
                f"{item['months_after_planting']}"
            )

        if "season" in item:
            print(f"   Season: {item['season']}")

        if "nutrients" in item:
            print(
                f"   Nutrients: "
                f"{', '.join(item['nutrients']) if item['nutrients'] else 'Monitoring'}"
            )

        print(f"   Recommendation: {item['recommendation']}")

        if "notes" in item:
            print(f"   Notes: {item['notes']}")

    print("\n" + "=" * 70)


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("Supported crops:")
    for crop in get_supported_crops():
        print("-", crop)

    print("\n")

    # Example
    print_schedule("rice")