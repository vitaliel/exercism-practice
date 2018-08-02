defmodule RNATranscription do
  @doc """
  Transcribes a character list representing DNA nucleotides to RNA

  ## Examples

  iex> RNATranscription.to_rna('ACTG')
  'UGAC'
  """
  @spec to_rna([char]) :: [char]
  def to_rna(dna) do
    for << ch <- List.to_string(dna) >>, do: transcribe(ch)
  end

  defp transcribe(?A), do: ?U
  defp transcribe(?C), do: ?G
  defp transcribe(?G), do: ?C
  defp transcribe(?T), do: ?A
end
