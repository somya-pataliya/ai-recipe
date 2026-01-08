app.post("/recipe", async (req, res) => {
  const { ingredients } = req.body;

  if (!ingredients) {
    return res.status(400).json({ error: "Ingredients missing" });
  }

  try {
    const response = await openai.responses.create({
      model: "gpt-4o-mini",
      input: `Create a simple step-by-step recipe using these ingredients: ${ingredients}`
    });

    res.json({
      recipe: response.output_text
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "AI generation failed" });
  }
});
