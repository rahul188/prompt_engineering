AGENDA_POINTS_SUMMARY_PROMPT = """   
[INST]
Role: You are the Company Secretary of a Fortune 500 corporation, expert in producing precise and comprehensive summaries for agenda items from board meeting transcripts and technical transcripts.

Task: Using your skills and experience in corporate governance and minute-taking, please generate a professional summary of the following meeting agenda items adhering to standard board meeting documentation practices.

CORE REQUIREMENTS:
1. Address ALL agenda items sequentially - no exceptions or combinations
2. Before starting, identify and confirm the total number of agenda items
3. For lengthy transcripts:
   - Map relevant sections to each agenda item by looking carefully in transcript lines
   - Process systematically, one agenda item at a time
4. Include ALL actually discussed information based on transcript
5. Format output as agenda items with summaries only
6. Maintain strict traceability to transcript
7. Summary for each agenda item should be STRICTLY in paragraph form
8. Use formal corporate language and terminology appropriately
9. Ensure financial values and figures are accurately extracted from the transcript
10. Do not include any speculative or inferred content

============================================================================================================
Transcript:
{{input_str}}
============================================================================================================

[/INST]
"""
#####

def agenda_document_points_prompt_implemention(agenda_items: List[str]) -> str:
    prompt = f"""
               [INST]
               Total Agenda Items to be Covered: {len(agenda_items)}

               Agenda Items:
               {', '.join(f"[{idx + 1}] {item}" for idx, item in enumerate(agenda_items))}

               SUMMARY GUIDELINES:
               1. Content must be traceable and relevant to transcript discussions
               2. Include context/background mentioned in transcript
               3. Preserve discussion chronology
               4. Use formal corporate language and terminology appropriately throughout your response
               5. Summary for each agenda item should be STRICTLY in paragraph form
               6. DO NOT include any timestamp information in your summary
               7. DO NOT use quotes directly from transcript
               8. Ensure financial values and figures are accurately extracted from the transcript
               9. Format output as agenda items with respective summaries only

               STRICTLY format your response for each agenda item as follows:
                        """

    for item in agenda_items:
        prompt += f"""
               {item}
               [Strictly ALWAYS provide a relevant, comprehensive formal summary in complete paragraph form for this agenda item such that it:
               - Captures ALL key points, key discussions, decisions; and USD values, financial figures and fund values related to this agenda item even if it is                mentioned briefly in transcript
               - Gives relevant information in the summary for this agenda item based on transcript
               - Maintains professional corporate minutes style. Use formal language naturally and appropriately
               - Uses phrases like "The Board noted", "pursuant to," "thereof," "herein," "whereby," etc. wherever necessary.
               - Includes ALL information from this specific agenda item based on transcript. Look carefully for information related to this agenda item in the                  transcript
               - Excludes speculative or inferred content
               - Exclude timestamp information in your summary
               - Omits additional sections like resolutions, notes etc.
               - Try to use minimum 150 words while ensuring traceability to transcript
               - Should be in paragraph form]
                            """

    prompt += """
               (STRICTLY follow the above format only)

               INSTRUCTIONS:
               - Confirm all agenda items are addressed
               - Verify every summary point traces to transcript
               - Check completeness and accuracy
               - DO NOT include this section in your response, or any other sections like 'resolution', 'note' etc.
               [/INST]
               """

    return prompt